from waapi import WaapiClient as _WaapiClient

from pywwise.enums import EObjectType
from pywwise.structs import ExternalSourceInfo, SoundBankInfo, SoundBankInclusions
from pywwise.types import Name, ShortID, GUID, ProjectPath, SystemPath


class SoundBank:
	"""ak.wwise.core.soundbank"""
	
	def __init__(self, client: _WaapiClient):
		"""
        Constructor.
        :param client: The WAAPI client to use.
        """
		self._client = client
	
	def convert_external_sources(self, sources: set[ExternalSourceInfo]) -> bool:
		"""
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_soundbank_convertexternalsources.html \n
        Converts the external sources files for the project as detailed in the wsources file, and places
        them into either the default folder, or the folder specified by the output argument. External
        Sources are a special type of source that you can put in a Sound object in Wwise. It indicates
        that the real sound data will be provided at run time. While External Source conversion is also
        triggered by SoundBank generation, this operation can be used to process sources not contained in
        the Wwise Project. Please refer to Wwise SDK help page "Integrating External Sources".
        :param sources: An array of external sources files and corresponding arguments.
        :return: Whether the call succeeded.
        """
		if sources is None:
			return False
		
		args = {"sources": list()}
		
		for source in sources:
			args["sources"].append(source.dictionary)
		
		return self._client.call("ak.wwise.core.soundbank.convertExternalSources", args) is not None
	
	def generate(self, sound_banks: set[SoundBankInfo] = None, platforms: set[GUID | Name] = None,
	             languages: set[GUID | Name] = None, clear_audio_file_cache: bool = False,
	             write_to_disk: bool = False, rebuild_init_bank: bool = False) -> dict:
		"""
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_soundbank_generate.html \n
        Generate a list of SoundBanks with the import definition specified in the WAAPI request. If you
        do not write the SoundBanks to disk, subscribe to `ak.wwise.core.soundbank.generated` to receive
        SoundBank structure info and the bank data as base64. Note: This is a synchronous operation.
        :param sound_banks: A list of SoundBanks to generate.
        :param platforms: A list of platforms to generate. By default, all platforms will be generated.
        :param languages: A list of languages to generate. By default, all languages will be generated. To skip
        languages, pass an empty set (`set()`) as the argument.
        :param clear_audio_file_cache: Deletes the content of the Wwise audio file cache folder prior to converting
        source files and generating SoundBanks, which ensures that all source files are reconverted.
        :param write_to_disk: Will write the sound bank and info file to disk.
        :param rebuild_init_bank: Use this option to force a rebuild of the Init bank for each specified platform.
        :return: The SoundBank generation log, as a dictionary. An empty dictionary means the log could not be
        retrieved.
        """
		args = dict()
		
		if sound_banks is not None:
			args["soundbanks"] = [sound_bank.dictionary for sound_bank in sound_banks]
		else:
			args["rebuildSoundBanks"] = True
		
		if platforms is not None:  # None = all platforms; no need to handle that here.
			args["platforms"] = [platform for platform in platforms]
		
		if languages is not None:  # None = all languages; no need to handle that here.
			if len(languages) > 0:  # specific languages
				args["languages"] = [language for language in languages]
			else:  # no languages; user explicitly passed an empty set
				args["skipLanguages"] = True
		
		args["clearAudioFileCache"] = clear_audio_file_cache
		args["writeToDisk"] = write_to_disk
		args["rebuildInitBank"] = rebuild_init_bank
		
		log = self._client.call("ak.wwise.core.soundbank.generate", args).get("logs")
		return log if log is not None else dict()
	
	def get_inclusions(self, sound_bank: Name | ShortID | GUID | ProjectPath):
		"""
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_soundbank_getinclusions.html \n
        Retrieves a SoundBank's inclusion list.
        :param sound_bank: The ID of the SoundBank to add an inclusion to.
        :return: An array of SoundBank inclusions.
        """
		args = {"soundbank": f"{EObjectType.SOUND_BANK.value}:{sound_bank}"}
		results = self._client.call("ak.wwise.core.soundbank.getInclusions", args)
		return results.get("object"), results.get("filter")
	
	def process_definition_files(self, files: set[SystemPath]) -> bool:
		"""
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_soundbank_processdefinitionfiles.html \n
        Imports SoundBank definitions from the specified file. Multiple files can be specified. See the
        WAAPI log for status messages.
        :param files: An array of SoundBank definition files.
        :return: Whether the call succeeded.
        """
		args = {"files": [str(file) for file in files]}
		return self._client.call("ak.wwise.core.soundbank.processDefinitionFiles", args) is not None
	
	def set_inclusions(self, sound_bank: Name | GUID | ProjectPath, operation: str,
	                   inclusions: set[SoundBankInclusions]):
		"""
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_soundbank_setinclusions.html \n
        Modifies a SoundBank's inclusion list. The 'operation' argument determines how the 'inclusions'
        argument modifies the SoundBank's inclusion list; 'inclusions' may be added to / removed from /
        replace the SoundBank's inclusion list.
        :param sound_bank: The ID of the SoundBank to add an inclusion to.
        :param operation: Determines how the 'inclusions' argument is used to modify the SoundBank's inclusion list.
        :param inclusions: An array of SoundBank inclusions.
        :return: Whether the call succeeded.
        """
		args = {"soundbank": f"{EObjectType.SOUND_BANK.value}:{sound_bank}", "operation": operation,
		        "inclusions": inclusions}
		return self._client.call("ak.wwise.core.soundbank.setInclusions", args) is not None
