# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from abc import ABC as _ABC
from enum import Enum as _Enum
from types import NoneType as _NoneType
from typing import Any as _Any, TypeVar as _TypeVar

from pywwise.enums import EObjectType
from pywwise.primitives import GUID, Name, ProjectPath
from pywwise.waapi.ak.ak import WwiseConnection


class WwiseObject(_ABC):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wobjects_index.html \n
    The base class for any class that serves as interface for getting/setting properties on Wwise objects.
    """
    
    def __init__(self, guid: GUID, ak: WwiseConnection,
                 platform: GUID | Name | _NoneType = None):
        """
        Uses a GUID to initialize a strongly-typed dynamic object, capable of fetching information from Wwise as needed.
        :param guid: If you may also pass a `WwiseObjectInfo` instance - this function will extract only the GUID.
        :param platform: If you want your object to only be used on a specific platform, specify which one here.
        """
        self._ak: WwiseConnection = ak
        self._guid: GUID = guid if isinstance(guid, GUID) else getattr(guid, "guid", GUID.get_null())
        self._query: str = f"$ from object \"{self._guid}\" take 1"
        self._platform = platform
    
    def get_property(self, name: str, default: _Any = None) -> _NoneType | bool | int | float | str | GUID | _Enum:
        """
        Gets the value of a property, reference, or list from this object in Wwise.
        :param name: The name of the property, reference, or list.
        :param default: The default value, in case retrieving the value fails.
        :return: The value of the property. This *can* be `None`.
        """
        info = self._ak.wwise.core.object.get(self._query, (name,))[0]
        return info.other.get(name, default)
    
    def set_property(self, name: str, value: _Any, is_reference: bool = False):
        if not is_reference:
            self._ak.wwise.core.object.set_property(self._guid, name, value, self._platform)
        else:
            self._ak.wwise.core.object.set_reference(self._guid, name, value, self._platform)
    
    @property
    def guid(self) -> GUID:
        """
        Get GUID.
        :return: Current GUID.
        """
        return self._guid
    
    @property
    def name(self) -> Name:
        """
        Get name.
        :return: Current name.
        """
        return self._ak.wwise.core.object.get(self._query)[0].name
    
    @name.setter
    def name(self, name: Name | str):
        """
        Set name.
        :param name: New name.
        """
        self._ak.wwise.core.object.set_name(self._guid, name)
    
    @property
    def path(self) -> ProjectPath:
        """
        Get path.
        :return: Current path.
        """
        return self._ak.wwise.core.object.get(self._query)[0].path
    
    @path.setter
    def path(self, path: ProjectPath):
        """
        Set path.
        :param path: New path.
        """
        if path[-1] == '\\':  # ProjectPath always uses `\\` instead of `/`.
            path = path[:-1]  # Remove slash.
        tokens = path.split('\\')
        if tokens[-1] == self.name:  # We only need the path up to the parent.
            path = tokens[:-1]  # Remove name.
        self._ak.wwise.core.object.move(self.guid, path)
    
    @property
    def type(self) -> EObjectType:
        """
        Get type.
        :return: The type.
        """
        return self._ak.wwise.core.object.get(self._query)[0].type


WwiseObjectType = _TypeVar("WwiseObjectType", bound=WwiseObject)
