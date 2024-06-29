from waapi import WaapiClient as _WaapiClient
from simplevent import RefEvent as _RefEvent
from pywwise.types import GUID, Name, ProjectPath
from pywwise.decorators import callback
from pywwise.enums import EReturnOptions


class Audio:
	"""ak.wwise.core.audio"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
		
		self.imported = _RefEvent()
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_audio_imported.html
		\nSent at the end of an import operation.
		\n**Event Data**:
		\n- The operation applied for the import.
		\n- A tuple of WwiseObjectInfo instances, representing objects created as part of the import operation.
		"""
		
		imported_args = {"return": [EReturnOptions.GUID, EReturnOptions.NAME, EReturnOptions.TYPE, EReturnOptions.PATH]}
		self._imported = self._client.subscribe("ak.wwise.core.audio.imported", self._on_imported, imported_args)
	
	@callback
	def _on_imported(self, **kwargs):
		"""
		Callback function for the `imported` event.
		:param kwargs: The event data.
		"""
		# operation =
	
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
