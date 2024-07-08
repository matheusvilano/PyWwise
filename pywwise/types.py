from pathlib import Path as _Path
from typing import Literal as _Literal, TypeAlias as _TypeAlias
from uuid import UUID as _UUID

SystemPath: _TypeAlias = _Path


class Name(str):
	"""A Wwise object Name. This is usually intended to be used with unique objects (e.g. State Groups)."""
	
	def __new__(cls, name):
		if len(name) <= 0:
			raise ValueError("The provided name string is empty.")
		return str.__new__(cls, name)
	
	@classmethod
	def get_null(cls) -> _Literal["\0"]:
		return "\0"


class GUID(str):
	"""A Wwise object GUID (e.g. `"{63726145-57FB-490B-B611-738BD3EF2F72}"`."""
	
	def __new__(cls, guid: str):
		if (guid[0] != '{' or guid[-1] != '}') or not cls.validate(guid):
			raise ValueError(f"Wrong GUID format. Expected format is: \"{cls.get_zero()}\" (alphanumerical).")
		return str.__new__(cls, guid)
	
	@classmethod
	def validate(cls, value: str):
		try:
			_UUID(value, version=4)
			return True
		except ValueError:
			return False
	
	@staticmethod
	def get_zero() -> _Literal["{00000000-0000-0000-0000-000000000000}"]:
		""":return: A string containing the default "zero" GUID."""
		return "{00000000-0000-0000-0000-000000000000}"


class ProjectPath(str):
	"""A project path (e.g. `"/Actor-Mixer Hierarchy/Default Work Unit/MyActorMixer"`)."""
	
	def __new__(cls, path: str):
		"""
		Creates a new ProjectPath. You can think of this as a string container.
		:param path: The project path of the Wwise object.
		"""
		if len(path) <= 0:
			raise ValueError("The provided path is empty. Must be a valid path-like string.")
		return str.__new__(cls, path)


class ShortID(int):
	"""A Wwise object short ID. This is expected to be a non-negative number."""
	
	def __new__(cls, value: int):
		"""
		Creates a new ShortID.
		:param value: The short ID of the Wwise object.
		"""
		if value < 0 and value != -1:
			raise ValueError("ShortID value must be non-negative (or -1, if representing an invalid ShortID).")
		return int.__new__(cls, value)
	
	@classmethod
	def get_invalid(cls) -> _Literal[-1]:
		"""
		Use when the intention is to represent an "invalid" short ID.
		:return: `-1`, which represents an invalid playing ID.
		"""
		return -1


class GameObjectID(int):
	"""A Game Object ID. This is expected to be a non-negative number."""
	
	def __new__(cls, obj_id: int):
		"""
		Creates a new GameObjectID. This does not register a new GameObject in Wwise.
		:param obj_id: The ID of the game object.
		"""
		if obj_id < 0 and obj_id != -1:
			raise ValueError("GameObject value must be non-negative (or -1 if representing an invalid ID).")
		return int.__new__(cls, obj_id)
	
	@classmethod
	def get_global(cls) -> int:
		"""
		Specialized factory function. Useful for scripts that target all game objects.
		:return: A new GameObjectID containing the default Global game object ID.
		"""
		return int.__new__(cls, (1 << 64) - 1)  # That expression equals the max uint64 value.
	
	@classmethod
	def get_transport(cls) -> int:
		"""
		Specialized factory function. Useful for scripts where the target game object is Wwise's transport.
		:return: A new GameObjectID containing the default Transport game object ID.
		"""
		return int.__new__(cls, (1 << 64) - 2)  # That expression equals the max uint64 value - 1.
	
	@classmethod
	def get_invalid(cls) -> _Literal[-1]:
		"""
		Use when the intention is to represent an "invalid" game object ID.
		:return: `-1`, which represents an invalid game object ID.
		"""
		return -1


class PlayingID(int):
	"""A Playing ID, which represents an instance generated from an Event. A negative means the ID is invalid."""
	
	@classmethod
	def get_invalid(cls) -> _Literal[-1]:
		"""
		Use when the intention is to represent an "invalid" playing ID.
		:return: `-1`, which represents an invalid playing ID.
		"""
		return -1
