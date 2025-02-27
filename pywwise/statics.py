# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from enum import Enum as _Enum
from re import findall as _re_findall, match as _re_match, split as _re_split
from typing import Any as _Any, Type as _Type, TypeVar as _TypeVar

from pywwise.metas import StaticMeta
from pywwise.modules import LazyModule

_EnumType = _TypeVar("_EnumType", bound=_Enum)
_pywwise_enums = LazyModule("pywwise.enums")  # To avoid circular imports.


class EnumStatics(metaclass=StaticMeta):
    """A static class containing useful utility functions for enums."""
    
    @staticmethod
    def from_value(enum_type: _Type[_EnumType], enum_value: _Any) -> _EnumType:
        """
        Gets an enum member whose value matches the provided value.
        :param enum_type: The enum type to run the search on.
        :param enum_value: The value to search for.
        :raise: ValueError, if the provided value does not exist in the enum type.
        :return: An enum member instance.
        """
        for member in enum_type:
            if member == enum_value:
                return member
        raise ValueError(f"No {_EnumType.__name__} member with value {enum_value}")
    
    @staticmethod
    def get_all_members(enum_type: _Type[_EnumType]) -> tuple[_EnumType, ...]:
        """
        Gets all members of an enum type.
        :param enum_type: The enum type to get all members from.
        :return: A tuple containing all members of an enum type.
        """
        return tuple(member for member in enum_type)


class StringStatics(metaclass=StaticMeta):
    """A static class containing useful utility functions for strings."""
    
    @staticmethod
    def validate_case(text: str) -> bool:
        """
        Checks if the provided string matches one of the common case styles (Snake, Camel, Pascal, etc.). Those are
        enumerated in `pywwise.enums.ECaseStyle`.
        :param text: The string to validate.
        :return: Whether the string is formatted in accordance to one of the common case styles (see
                 `pywwise.enums.ECaseStyle` for a complete list).
        """
        for case in _pywwise_enums.ECaseStyle:
            if _re_match(case, text):
                return True
        return False
    
    @staticmethod
    def to_camel_case(text: str) -> str:
        """
        Converts text to camelCase, to the best possible extent.
        :param text: The string to convert to camelCase.
        :return: The string, with the camelCase format.
        """
        if _re_match(_pywwise_enums.ECaseStyle.CAMEL, text):
            return text
        tokens = _re_split(r"[-_\s]", text)
        if tokens == [text]:  # Handle PascalCase or camelCase
            tokens = _re_findall(r"[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)", text)
        return tokens[0].lower() + ''.join(x.title() for x in tokens[1:])  # Convert to camelCase
    
    @staticmethod
    def to_kebab_case(text: str) -> str:
        """
        Converts text to kebab-case, to the best possible extent.
        :param text: The string to convert to kebab-case.
        :return: The string, with the kebab-case format.
        """
        if _re_match(_pywwise_enums.ECaseStyle.KEBAB, text):
            return text
        if _re_match(_pywwise_enums.ECaseStyle.PASCAL, text) or _re_match(_pywwise_enums.ECaseStyle.CAMEL, text):
            tokens = _re_findall(r"[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)", text)
        else:
            tokens = _re_split(r"[-_\s]", text)
        return '-'.join([token.lower() for token in tokens])
    
    @staticmethod
    def to_pascal_case(text: str) -> str:
        """
        Converts text to PascalCase, to the best possible extent.
        :param text: The string to convert to PascalCase.
        :return: The string, with the PascalCase format.
        """
        if _re_match(_pywwise_enums.ECaseStyle.PASCAL, text):
            return text
        as_camel = StringStatics.to_camel_case(text)
        return f"{as_camel[0].upper()}{as_camel[1:]}"
    
    @staticmethod
    def to_snake_case(text: str) -> str:
        """
        Converts text to snake_case, to the best possible extent.
        :param text: The string to convert to snake_case.
        :return: The string, with the snake_case format.
        """
        if _re_match(_pywwise_enums.ECaseStyle.SNAKE, text):
            return text
        return StringStatics.to_kebab_case(text).replace('-', '_')
    
    @staticmethod
    def to_upper_case(text: str) -> str:
        """
        Converts text to UPPER_CASE, to the best possible extent.
        :param text: The string to convert to UPPER_CASE.
        :return: The string, with the UPPER_CASE format.
        """
        if _re_match(_pywwise_enums.ECaseStyle.UPPER, text):
            return text
        return StringStatics.to_snake_case(text).upper()


class JsonStatics(metaclass=StaticMeta):
    """A static class containing useful utility functions for dictionaries that represent JSON objects."""
    
    @staticmethod
    def from_object(obj: _Any) -> dict:
        """
        Creates a JSON-like dictionary based on the provided object's `__dict__`.
        :param obj: The object to use when creating the dictionary.
        :return: A JSON-like dictionary representing the provided object.
        :raise: NotImplementedError - this function is tentative and is still in the works.
        """
        raise NotImplementedError("This function is not implemented yet. For this functionality, try using the "
                                  "`dictionary` property of structs, if available.")
