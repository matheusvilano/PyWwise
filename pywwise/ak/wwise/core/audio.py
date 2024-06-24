from waapi import WaapiClient as _WaapiClient
from pywwise.types import Name as _Name, ShortID as _ShortID, GUID as _GUID, GameObjectID as _GameObjectID, \
	ProjectPath as _ProjectPath, PlayingID as _PlayingID


class Audio:
	"""ak.wwise.core.audio"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
	
	def import_files(self):
		"""
		Creates Wwise objects and imports audio files. This function does not return an error when
		something fails during the import process, please refer to the log for the result of each import
		command. This function uses the same importation processor available through the Tab Delimited
		import in the Audio File Importer. The function returns an array of all objects created,
		replaced or re-used. Use the options to specify how the objects are returned. For more
		information, refer to Importing Audio Files and Creating Structures.
		"""
		# "import" is a reserved keyword, so function name does not match WAAPI
	
	def import_tab_delimited(self):
		"""
		Scripted object creation and audio file import from a tab-delimited file.
		"""
	
	def mute(self, objects: set[_GUID | _Name | _ProjectPath], value: bool) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_audio_mute.html \n
		Mute or unmute objects.
		:param objects: The GUID, Name, or Project Path of the objects to mute. Using Names is supported for object
		types that have unique names (e.g. Buses, Events, etc.), but it is still NOT recommended. If you choose to use
		Names, you will have to specify the type of the object (e.g. `Name("Event:Play_Footstep")`).
		:param value: Whether the objects should be muted or not.
		:return: Whether the call succeeded. True does not necessarily mean objects were muted/unmuted successfully.
		"""
		args = {"objects": list(objects), "value": value}
		return self._client.call("ak.wwise.core.audio.mute", args) is not None
		
	def reset_mute(self) -> bool:
		"""
		Unmute all muted objects.
		:return: Whether the call succeeded. True does not necessarily mean objects were unmuted successfully.
		"""
		return self._client.call("ak.wwise.core.audio.resetMute") is not None
	
	def reset_solo(self) -> bool:
		"""
		Unsolo all soloed objects.
		:return: Whether the call succeeded. True does not necessarily mean objects were unsoloed successfully.
		"""
		return self._client.call("ak.wwise.core.audio.resetSolo") is not None
	
	def solo(self, objects: set[_GUID | _Name | _ProjectPath], value: bool):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_audio_solo.html \n
		Solos an object.
		:param objects: The GUID, Name, or Project Path of the objects to solo. Using Names is supported for object
		types that have unique names (e.g. Buses, Events, etc.), but it is still NOT recommended. If you choose to use
		Names, you will have to specify the type of the object (e.g. `Name("Event:Play_Footstep")`).
		:param value: Whether the object is soloed or not. 1 is true, 0 is false.
		:return: Whether the call succeeded. True does not necessarily mean objects were soloed/unsoloed successfully.
		"""
		args = {"objects": list(objects), "value": value}
		return self._client.call("ak.wwise.core.audio.solo", args) is not None
