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
    """A descriptor for Wwise properties, references, and lists."""
    
    def __init__(self, name: str, etype: _Type):
        self._name = name
        self._type = etype
    
    def __get__(self, instance, owner) -> _T:
        getter = getattr(instance, "get_property")
        if getter is None:
            TypeError("The owner of WwiseProperty must implement the `get_property` function.")
        value = getter(self._name)
        return value if not issubclass(self._type, _Enum) else EnumStatics.from_value(self._type, value)
    
    def __set__(self, instance, value: _T):
        setter = getattr(instance, "set_property")
        if setter is None:
            TypeError("The owner of WwiseProperty must implement the `set_property` function.")
        if issubclass(value.__class__, pywwise.objects.WwiseObject) or isinstance(value, WwiseObjectInfo):
            value = value.guid
        instance.set_property(self._name, value, isinstance(value, GUID))
