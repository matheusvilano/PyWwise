from waapi import WaapiClient as _WaapiClient
from pywwise.structs import ExternalSourceInfo as _ExternalSourceInfo
from pywwise.types import Name as _Name, ShortID as _ShortID, GUID as _GUID, ProjectPath as _ProjectPath, FilePath as _FilePath

class SoundBank:
    """ak.wwise.core.soundbank"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def convert_external_sources(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_soundbank_convertexternalsources.html \n
        Converts the external sources files for the project as detailed in the wsources file, and places
        them into either the default folder, or the folder specified by the output argument. External
        Sources are a special type of source that you can put in a Sound object in Wwise. It indicates
        that the real sound data will be provided at run time. While External Source conversion is also
        triggered by SoundBank generation, this operation can be used to process sources not contained in
        the Wwise Project. Please refer to Wwise SDK help page "Integrating External Sources".
        :param sources: An array of external sources files and corresponding arguments.
        :param input: The path to the wsources file.
        :param platform: The platform to convert external sources for.
        :param output: Optional argument for the path of the output folder to be generated.
        :return: Whether the call succeeded.
        """

    def generate(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_soundbank_generate.html \n
        Generate a list of SoundBanks with the import definition specified in the WAAPI request. If you
        do not write the SoundBanks to disk, subscribe to `ak.wwise.core.soundbank.generated` to receive
        SoundBank structure info and the bank data as base64. Note: This is a synchronous operation.
        """

    def get_inclusions(self, soundbank: _Name | _ShortID | _GUID | _ProjectPath):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_soundbank_getinclusions.html \n
        Retrieves a SoundBank's inclusion list.
        :param soundbank: The ID of the SoundBank to add an inclusion for.
        :return: An array of SoundBank inclusions.
        """
        args = {"soundbank": soundbank}
        results =  self._client.call("ak.wwise.core.soundbank.getInclusions", args).get("return")

    def process_definition_files(self, files: set[_FilePath]) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_soundbank_processdefinitionfiles.html \n
        Imports SoundBank definitions from the specified file. Multiple files can be specified. See the
        WAAPI log for status messages.
        :param files: An array of SoundBank definition files.
        :return: Whether the call succeeded.
        """
        args = {"files": list(files), "numFiles": len(files)}
        results = self._client.call("ak.wwise.core.soundbank.processDefinitionFiles", args) is not None

    def set_inclusions(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_soundbank_setinclusions.html \n
        Modifies a SoundBank's inclusion list. The 'operation' argument determines how the 'inclusions'
        argument modifies the SoundBank's inclusion list; 'inclusions' may be added to / removed from /
        replace the SoundBank's inclusion list.
        """
