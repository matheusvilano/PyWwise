from pathlib import Path as _Path
from typing import TypeAlias as _TypeAlias, Self as _Self
from uuid import UUID as _UUID

SystemPath: _TypeAlias = _Path


class Name(str):
	"""A Wwise object Name. This is usually intended to be used with unique objects (e.g. State Groups)."""
	
	def __new__(cls, name: str) -> str:
		"""
		Instantiates a new Name.
		:param name: The string to use to create a new Name.
		:return: The new Name.
		:raises ValueError: If the name is empty.
		"""
		if len(name) <= 0:
			raise ValueError("The provided name string is empty.")
		return str.__new__(cls, name)
	
	@classmethod
	def get_null(cls) -> _Self:
		"""
		Gets a "null" Name. Use this to represent an "invalid" Name.
		:return: A Name containing the null-terminator character (`\0`), which represents a "null" Name.
		"""
		return Name("\0")


class GUID(str):
	"""A Wwise object GUID (e.g. `"{63726145-57FB-490B-B611-738BD3EF2F72}"`."""
	
	def __new__(cls, guid: str) -> str:
		"""
		Instantiates a new GUID.
		:param guid: The string to use to create a new GUID.
		:return: The new GUID.
		:raise ValueError: If the GUID is in the wrong format.
		"""
		if (guid[0] != '{' or guid[-1] != '}') or not cls.validate(guid):
			raise ValueError(f"Wrong GUID format. Expected format is: \"{cls.get_zero()}\" (alphanumerical).")
		return str.__new__(cls, guid)
	
	@classmethod
	def validate(cls, value: str) -> bool:
		"""
		Validates the provided string as a GUID.
		:param value: The string to validate as a GUID.
		:return: Whether the provided string is a valid GUID.
		"""
		try:
			_UUID(value, version=4)
			return True
		except ValueError:
			return False
	
	@classmethod
	def get_zero(cls) -> _Self:
		"""
		A GUID containing "zero" (the default "invalid" GUID).
		:return: The GUID "{00000000-0000-0000-0000-000000000000}".
		"""
		zero = "{00000000-0000-0000-0000-000000000000}"
		return GUID(zero)


class ProjectPath(str):
	"""A project path (e.g. `"/Actor-Mixer Hierarchy/Default Work Unit/MyActorMixer"`)."""
	
	def __new__(cls, path: str) -> str:
		"""
		Creates a new ProjectPath. You can think of this as a string container.
		:param path: The project path of the Wwise object.
		:return: A new ProjectPath.
		:raise ValueError: If the path is empty.
		"""
		if len(path) <= 0:
			raise ValueError("The provided path is empty. Must be a valid path-like string.")
		return str.__new__(cls, path)


class ShortID(int):
	"""A Wwise object short ID. This is expected to be a non-negative number."""
	
	def __new__(cls, value: int) -> int:
		"""
		Creates a new ShortID.
		:param value: The short ID of the Wwise object.
		:return: The new ShortID.
		:raise ValueError: If the short ID is less than `0` and not `-1`.
		"""
		if value < 0 and value != -1:
			raise ValueError("ShortID value must be non-negative (or -1, if representing an invalid ShortID).")
		return int.__new__(cls, value)
	
	@classmethod
	def get_invalid(cls) -> _Self:
		"""
		Use when the intention is to represent an "invalid" short ID.
		:return: `-1`, which represents an invalid short ID.
		"""
		return ShortID(-1)
	
	def is_valid(self) -> bool:
		"""
		Checks whether the short ID is valid.
		:return: `True`, if the short ID is valid; else, `False`.
		"""
		return int(self) != -1  # or greater than or equal to 0


class GameObjectID(int):
	"""A Game Object ID. This is expected to be a non-negative number."""
	
	def __new__(cls, obj_id: int) -> int:
		"""
		Creates a new GameObjectID. This does not register a new GameObject in Wwise.
		:param obj_id: The ID of the game object.
		:return: The new GameObjectID.
		:raise ValueError: If the game object ID is invalid.
		"""
		if obj_id < 0 and obj_id != -1:
			raise ValueError("GameObject value must be non-negative (or -1 if representing an invalid ID).")
		return int.__new__(cls, obj_id)
	
	@classmethod
	def get_global(cls) -> _Self:
		"""
		Specialized factory function. Useful for scripts that target all game objects.
		:return: A new GameObjectID containing the default Global game object ID.
		"""
		return GameObjectID((1 << 64) - 1)  # That expression equals the max uint64 value.
	
	@classmethod
	def get_transport(cls) -> _Self:
		"""
		Specialized factory function. Useful for scripts where the target game object is Wwise's transport.
		:return: A new GameObjectID containing the default Transport game object ID.
		"""
		return GameObjectID((1 << 64) - 2)  # That expression equals the max uint64 value - 1.
	
	@classmethod
	def get_invalid(cls) -> _Self:
		"""
		Use when the intention is to represent an "invalid" game object ID.
		:return: `-1`, which represents an invalid game object ID.
		"""
		return GameObjectID(-1)
	
	def is_valid(self) -> bool:
		"""
		Checks whether the game object ID is valid.
		:return: `True`, if the game object ID is valid; else, `False`.
		"""
		return int(self) != -1  # or greater than or equal to 0


class PlayingID(int):
	"""A Playing ID, which represents an instance generated from an Event. A negative means the ID is invalid."""
	
	@classmethod
	def get_invalid(cls) -> _Self:
		"""
		Use when the intention is to represent an "invalid" playing ID.
		:return: `-1`, which represents an invalid playing ID.
		"""
		return PlayingID(-1)
	
	def is_valid(self) -> bool:
		"""
		Checks whether the playing ID is valid.
		:return: `True`, if the playing ID is valid; else, `False`.
		"""
		return int(self) != -1  # or greater than or equal to 0
