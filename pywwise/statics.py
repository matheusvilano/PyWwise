from enum import Enum as _Enum
from typing import TypeVar as _TypeVar, Type as _Type, Any as _Any

_EnumType = _TypeVar("_EnumType", bound=_Enum)


class EnumUtils:
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


class JsonUtils:
	"""A static class containing useful utility functions for dictionaries that represent JSON objects."""

	@staticmethod
	def from_object(obj: _Any):
		raise NotImplementedError("This function is not implemented yet. For this functionality, try using the "
		                          "`dictionary` property of structs, if available.")
