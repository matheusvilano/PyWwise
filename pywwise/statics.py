from enum import Enum as _Enum
from re import findall as _re_findall, match as _re_match, split as _re_split
from typing import Any as _Any, Type as _Type, TypeVar as _TypeVar
from pywwise.enums import ECaseStyle
from pywwise.metas import StaticMeta

_EnumType = _TypeVar("_EnumType", bound=_Enum)


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
