from waapi import WaapiClient as _WaapiClient
from simplevent import RefEvent as _RefEvent
from pywwise.decorators import callback
from pywwise.enums import ELogSeverity, EReturnOptions
from pywwise.statics import EnumStatics
from pywwise.structs import LogItem, SoundBankData, SoundBankGenerationInfo, WwiseObjectInfo
from pywwise.types import Name


class SoundBank:
	"""ak.wwise.core.soundbank"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
		
		self.generated = _RefEvent(SoundBankGenerationInfo)
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_soundbank_generated.html
		\nSent when a SoundBank is generated. Can multi-trigger during SoundBank generation, per bank and per platform.
		\n**Event Data**:
		\n- A SoundBankGenerationInfo instance, which contains information about the generated SoundBank.
		"""
		
		generated_args = {"infoFile": True, "bankData": True, "pluginInfo": True,
		                  "return": [EReturnOptions.GUID, EReturnOptions.NAME,
		                             EReturnOptions.TYPE, EReturnOptions.PATH]}
		
		self._generated = self._client.subscribe("ak.wwise.core.soundbank.generated",
		                                         self._on_generated, generated_args)
		
		self.generation_done = _RefEvent(tuple[LogItem])
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_soundbank_generationdone.html
		\nSent when all SoundBanks are generated. Do not use to check if `ak.wwise.core.soundbank.generate` has completed.
		\n**Event Data**:
		\n- A tuple of LogItems representing the SoundBank generation log. Empty when used in WwiseConsole.
		"""
		
		self._generation_done = self._client.subscribe("ak.wwise.core.soundbank.generationDone",
		                                               self._on_generation_done)
	
	@callback
	def _on_generated(self, **kwargs):
		"""
		Callback function for the `generated` event.
		:param kwargs: The event data.
		"""
		sound_bank = kwargs["soundbank"]
		sound_bank = WwiseObjectInfo(sound_bank["id"], sound_bank["name"], sound_bank["type"], sound_bank["path"])
		platform = Name(kwargs["platform"]["name"])
		language = Name(kwargs["language"]) if kwargs.get("language") is not None else Name.get_null()
		bank_data = kwargs.get("bankData", dict())
		bank_data = SoundBankData(bank_data.get("data", ""), bank_data.get("size", 0))
		banks_info = kwargs.get("bankInfo", list())
		plugins_info = kwargs.get("pluginInfo", dict())
		error_message = kwargs.get("error", "")
		self.generated(SoundBankGenerationInfo(sound_bank, platform, language, bank_data,
		                                       banks_info, plugins_info, error_message))
	
	@callback
	def _on_generation_done(self, **kwargs):
		"""
		Callback function for the `generationDone` event.
		:param kwargs: The event data.
		"""
		items = [LogItem(severity=EnumStatics.from_value(ELogSeverity, item["severity"]), time=item["time"],
		                 id=item["messageId"], description=item["message"]) for item in kwargs.get("logs", ())]
		self.generation_done(tuple(items))
	
	def convert_external_sources(self):
		"""
		Converts the external sources files for the project as detailed in the wsources file, and places
		them into either the default folder, or the folder specified by the output argument. External
		Sources are a special type of source that you can put in a Sound object in Wwise. It indicates
		that the real sound data will be provided at run time. While External Source conversion is also
		triggered by SoundBank generation, this operation can be used to process sources not contained in
		the Wwise Project. Please refer to Wwise SDK help page "Integrating External Sources".
		"""
	
	def generate(self):
		"""
		Generate a list of SoundBanks with the import definition specified in the WAAPI request. If you
		do not write the SoundBanks to disk, subscribe to `ak.wwise.core.soundbank.generated` to receive
		SoundBank structure info and the bank data as base64. Note: This is a synchronous operation.
		"""
	
	def get_inclusions(self):
		"""
		Retrieves a SoundBank's inclusion list.
		"""
	
	def process_definition_files(self):
		"""
		Imports SoundBank definitions from the specified file. Multiple files can be specified. See the
		WAAPI log for status messages.
		"""
	
	def set_inclusions(self):
		"""
		Modifies a SoundBank's inclusion list. The 'operation' argument determines how the 'inclusions'
		argument modifies the SoundBank's inclusion list; 'inclusions' may be added to / removed from /
		replace the SoundBank's inclusion list.
		"""
