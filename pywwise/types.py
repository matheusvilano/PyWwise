class Name(str):
	"""A Wwise object Name. This is usually intended to be used with unique objects (e.g. State Groups)."""
	
	def __new__(cls, name):
		if len(name) <= 0:
			raise ValueError("The provided name string is empty.")
		return str.__new__(cls, name)


class GUID(str):
	"""A Wwise object GUID (e.g. `"{63726145-57FB-490B-B611-738BD3EF2F72}"`."""
	
	def __new__(cls, guid: str):
		if len(guid) != 38:
			raise ValueError("GUID string must have exactly 38 characters.")
		if guid[0] != '{' or guid[-1] != '}':
			raise ValueError(
				"GUID string format is incorrect. The string must be enclosed in curly brackets ('{' and '}').")
		if guid[9] != '-' or guid[14] != '-' or guid[19] != '-' or guid[24] != '-':
			raise ValueError(
				"GUID string format is incorrect. Indexes 9, 14, 19, and 24 should all contain a dash (`-`).")
		return str.__new__(cls, guid)


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
		if value < 0:
			raise ValueError("ShortID value must be non-negative.")
		return int.__new__(cls, value)


class GameObjectID(int):
	"""A Game Object ID. This is expected to be a non-negative number."""
	
	def __new__(cls, obj_id: int):
		"""
		Creates a new GameObjectID. This does not register a new GameObject in Wwise.
		:param obj_id: The ID of the game object.
		"""
		if obj_id < 0:
			raise ValueError("GameObject value must be non-negative")
		return int.__new__(cls, obj_id)
	
	@classmethod
	def get_global(cls):
		"""
		Specialized factory function. Useful for scripts that target all game objects.
		:return: A new GameObjectID containing the default Global game object ID.
		"""
		return int.__new__(cls, (1 << 64) - 1)  # That expression equals the max uint64 value.
	
	@classmethod
	def get_transport(cls):
		"""
		Specialized factory function. Useful for scripts where the target game object is Wwise's transport.
		:return: A new GameObjectID containing the default Transport game object ID.
		"""
		return int.__new__(cls, (1 << 64) - 2)  # That expression equals the max uint64 value - 1.


class PlayingID(int):
	"""A Playing ID, which represents an instance generated from an Event. A negative means the ID is invalid."""
