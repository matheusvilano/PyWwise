# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from enum import Enum as _Enum
from typing import Generic as _Generic, Type as _Type, TypeVar as _TypeVar

import pywwise.objects  # Requires full import to avoid circular import.
from pywwise.primitives import GUID
from pywwise.statics import EnumStatics
from pywwise.structs import WwiseObjectInfo

_T = _TypeVar("_T")


class WwiseProperty(_Generic[_T]):
    """A descriptor for Wwise properties, references, and lists. Supports the `WwiseProperty[Type] syntax to allow
    auto-completion and suggestions in interactive environments."""
    
    def __init__(self, name: str, etype: _Type[_T]):
        """
        Initializer.
        :param name: The name of the property.
        :param etype: The type of the property. If using the `WwiseProperty[Type]` syntax, this parameter MUST match
        the type specified in brackets. Due to a limitation in the Python syntax, this
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
            TypeError("An object encapsulating a WwiseProperty must implement the `get_property` function.")
        
        ak = getattr(instance, "_ak")
        if ak is None:
            TypeError("An object encapsulating a WwiseProperty must have a protected WwiseConnection called `_ak`.")
        
        value = getter(self._name)
        
        # If the return value is a WwiseObject, it will first be a JSON-like dictionary, which we need to process.
        if issubclass(self._type, pywwise.objects.WwiseObject) and isinstance(value, dict):
            return self._type(value.get("id", GUID.get_null()), ak)  # Return WwiseObject instead of dict.
        return value if not issubclass(self._type, _Enum) else EnumStatics.from_value(self._type, value)
    
    def __set__(self, instance, value: _T):
        """
        Setter.
        :param instance: The caller.
        :param value: The new value.
        """
        setter = getattr(instance, "set_property")
        if setter is None:
            TypeError("The owner of WwiseProperty must implement the `set_property` function.")
        if issubclass(value.__class__, pywwise.objects.WwiseObject) or isinstance(value, WwiseObjectInfo):
            value = value.guid
        instance.set_property(self._name, value, isinstance(value, GUID))

    @property
    def type(self) -> _Type[_T]:
        """:return: The type of this property."""
        return self._type
