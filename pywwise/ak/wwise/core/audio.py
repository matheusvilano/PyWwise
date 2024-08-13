from waapi import WaapiClient as _WaapiClient
from simplevent import RefEvent as _RefEvent
from pywwise.decorators import callback
from pywwise.enums import EReturnOptions, EImportOperation
from pywwise.statics import EnumStatics
from pywwise.structs import WwiseObjectInfo
from pywwise.aliases import SystemPath


class Audio:
	"""ak.wwise.core.audio"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
		
		self.imported = _RefEvent(EImportOperation, tuple[WwiseObjectInfo, ...], tuple[SystemPath, ...])
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_audio_imported.html
		\nSent at the end of an import operation.
		\n**Event Data**:
		\n- The operation applied for the import.
		\n- A tuple of WwiseObjectInfo instances, representing objects created as part of the import operation.
		\n- A tuple of SystemPath instances, representing the paths of the imported assets.
		"""
		
		imported_args = {"return": [EReturnOptions.GUID.value, EReturnOptions.NAME.value,
		                            EReturnOptions.TYPE.value, EReturnOptions.PATH.value]}
		self._imported = self._client.subscribe("ak.wwise.core.audio.imported", self._on_imported, imported_args)
	
	@callback
	def _on_imported(self, event: _RefEvent, **kwargs):
		"""
		Callback function for the `imported` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		objects = list[WwiseObjectInfo]()
		for obj in kwargs.get("objects", dict()):
			objects.append(WwiseObjectInfo.from_dict(obj))
		event(EnumStatics.from_value(EImportOperation, kwargs["operation"]), tuple(objects),
		      tuple([SystemPath(file) for file in kwargs.get("files", ())]))
	
	def import_files(self):
		"""
		Creates Wwise objects and imports audio files. This function does not return an error when
		something fails during the import process, please refer to the log for the result of each import
		command. This function uses the same importation processor available through the Tab Delimited
		import in the Audio File Importer. The function returns an array of all objects created,
		replaced or re-used. Use the options to specify how the objects are returned. For more
		information, refer to Importing Audio Files and Creating Structures.
		"""
	
	def import_tab_delimited(self):  # "import" is a reserved keyword; function name won't match WAAPI
		"""
		Scripted object creation and audio file import from a tab-delimited file.
		"""
	
	def mute(self):
		"""
		Mutes an object.
		"""
	
	def reset_mute(self):
		"""
		Unmute all muted objects.
		"""
	
	def reset_solo(self):
		"""
		Unsolo all soloed objects.
		"""
	
	def solo(self):
		"""
		Solos an object.
		"""
