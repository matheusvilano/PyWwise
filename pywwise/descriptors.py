# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from enum import Enum as _Enum
from typing import Generic as _Generic, Self as _Self, Type as _Type, TypeVar as _TypeVar

import pywwise.objects  # Requires full import to avoid circular import.
from pywwise.aliases import SystemPath
from pywwise.primitives import GUID
from pywwise.statics import EnumStatics
from pywwise.structs import WwiseObjectInfo

_T = _TypeVar("_T")


class WwiseProperty(_Generic[_T]):
    """A descriptor for Wwise properties, references, and lists. Supports the `WwiseProperty[Type]` syntax to allow
    auto-completion and suggestions in interactive environments."""
    
    def __init__(self, name: str, etype: _Type[_T]):
        """
        Initializer.
        :param name: The name of the property.
        :param etype: The type of the property. If using the `WwiseProperty[Type]` syntax, this parameter MUST match
        the type specified in brackets. Due to a limitation in the Python syntax, `etype` cannot be used for type hints.
        """
        self._name = name
        self._type = etype
    
    def __get__(self, instance, owner) -> _T:
        """
        Getter.
        :param instance: The caller.
        :param owner: The owner.
        :return: The current value.
        """
        getter = getattr(instance, "get_property")
        
        if getter is None:
            raise TypeError("Encapsulators of `WwiseProperty` must implement the `get_property` function.")
        
        ak = getattr(instance, "_ak")
        
        if ak is None:
            raise TypeError("Encapsulators of `WwiseProperty` must define a protected `WwiseConnection` named `_ak`.")
        
        value = getter(self._name)
        
        _type = self._type if self._type is not _Self else instance.__class__  # Class is referencing itself.
        
        match _type:  # Decide on what kind of object to return.
            
            case _ if issubclass(_type, pywwise.objects.WwiseObject) and isinstance(value, dict):  # WwiseObject
                return _type(value.get("id", GUID.get_null()), ak)
            
            case _ if issubclass(_type, _Enum):  # Any generic enum.Enum, but usually a pywwise.enums type.
                return EnumStatics.from_value(_type, value)
            
            case _:  # Anything else, including GUID, ProjectPath, GameObjectID, SystemPath, etc.
                return _type(value)  # PyCharm might throw a warning here about a missing `ak`; false negative.
    
    def __set__(self, instance, value: _T):
        """
        Setter.
        :param instance: The caller.
        :param value: The new value.
        """
        setter = getattr(instance, "set_property")
        
        if setter is None:
            raise TypeError("Encapsulators of WwiseProperty must implement the `set_property` function.")
        
        if issubclass(self._type, SystemPath):  # pathlib.Path (SystemPath) is not JSON-serializable; convert to `str`.
            value = str(value)
        elif issubclass(value.__class__, pywwise.objects.WwiseObject) or isinstance(value, WwiseObjectInfo):
            value = value.guid
        
        instance.set_property(self._name, value, isinstance(value, GUID))
    
    @property
    def type(self) -> _Type[_T]:
        """:return: The type of this property."""
        return self._type
