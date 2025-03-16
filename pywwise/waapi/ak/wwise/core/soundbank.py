# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient

from pywwise.aliases import ListOrTuple, SystemPath
from pywwise.decorators import callback
from pywwise.enums import (EGeneratedSoundBankType, EInclusionFilter, EInclusionOperation, ELogSeverity, EObjectType,
                           EReturnOptions)
from pywwise.primitives import GUID, Name, ProjectPath, ShortID
from pywwise.statics import EnumStatics
from pywwise.structs import (ExternalSourceInfo, LogItem, PluginLibraryInfo, SoundBankData, SoundBankGenerationInfo,
                             SoundBankInclusion, SoundBankInfo)


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
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_soundbank_generated.html
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
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_soundbank_generationdone.html
        \nSent when all SoundBanks are generated. Do not use to check if `ak.wwise.core.soundbank.generate` has completed.
        \n**Event Data**:
        \n- A tuple of LogItems representing the SoundBank generation log. Empty when used in WwiseConsole.
        """
        
        self._generation_done = self._client.subscribe("ak.wwise.core.soundbank.generationDone",
                                                       self._on_generation_done)
    
    @callback
    def _on_generated(self, event: _RefEvent, **kwargs):
        """
        Callback function for the `generated` event.
        :param event: The event to broadcast.
        :param kwargs: The event data.
        """
        # Key: soundBank
        bank = kwargs.get("soundbank", dict())
        guid = GUID(bank.get("id", GUID.get_null()))
        name = Name(bank.get("name", Name.get_null()))
        path = ProjectPath(bank.get("path", ProjectPath.get_null()))
        
        # Key: bankInfo
        info = kwargs.get("bankInfo", list[dict]())
        info = info[0] if info else dict()
        short = ShortID(info.get("Id", ShortID.get_null()))
        file = str(info.get("Path", ""))
        btype = EnumStatics.from_value(EGeneratedSoundBankType, info.get("Type", ""))
        bhash = GUID(info.get("Hash", GUID.get_null()))
        
        # Key: bankInfo.Media
        media = info.get("Media", dict())
        
        # Key: bankInfo.ExternalSources
        externals = info.get("ExternalSources", dict())
        
        # Key: bankInfo.Plugins
        plugins = info.get("Plugins", dict())
        
        # Key: bankInfo.Events
        events = info.get("Events", dict())
        
        # Key: bankInfo.DialogueEvents
        dialogues = info.get("DialogueEvents", dict())
        
        # Key: bankInfo.Busses
        busses = info.get("Busses", dict())
        
        # Key: bankInfo.AuxBusses
        auxes = info.get("AuxBusses", dict())
        
        # Key: bankInfo.GameParameters
        parameters = info.get("GameParameters", dict())
        
        # Key: bankInfo.Triggers
        triggers = info.get("Triggers", dict())
        
        # Key: bankInfo.StateGroups
        states = info.get("StateGroups", dict())
        
        # Key: bankInfo.SwitchGroups
        switches = info.get("SwitchGroups", dict())
        
        # Key: bankInfo.AcousticTextures
        textures = info.get("AcousticTextures", dict())
        
        # Key: pluginInfo
        libs = kwargs.get("pluginInfo", dict()).get("PluginLibs", list[dict]())
        libs = [PluginLibraryInfo(str(lib.get("LibName", "")), ShortID(lib.get("LibId", ShortID.get_null())),
                                  str(lib.get("Type", "")), str(lib.get("DLL", "")), str(lib.get("StaticLib", "")))
                for lib in libs]
        libs = tuple(libs)
        
        # Key: bankData
        bank_data = kwargs.get("bankData", dict())
        bank_data = SoundBankData(bank_data.get("data", ""), bank_data.get("size", 0))
        
        # Other data
        error_message = kwargs.get("error", "")
        platform = Name(kwargs.get("platform", dict()).get("name", Name.get_null()))
        language = Name(kwargs.get("language", Name.get_null()))
        
        event(SoundBankGenerationInfo(guid, name, path, file, short, bhash, btype, platform, language, media, externals,
                                      plugins, events, dialogues, busses, auxes, parameters, triggers, states, switches,
                                      textures, bank_data, libs, error_message))
    
    @callback
    def _on_generation_done(self, event: _RefEvent, **kwargs):
        """
        Callback function for the `generationDone` event.
        :param event: The event to broadcast.
        :param kwargs: The event data.
        """
        items = [LogItem(severity=EnumStatics.from_value(ELogSeverity, item["severity"]), time=item["time"],
                         id=item["messageId"], description=item["message"]) for item in kwargs.get("logs", ())]
        event(tuple(items))
    
    def convert_external_sources(self, sources: ListOrTuple[ExternalSourceInfo]) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_soundbank_convertexternalsources.html \n
        Converts the external sources files for the project as detailed in the wsources file, and places
        them into either the default folder, or the folder specified by the output argument. External
        Sources are a special type of source that you can put in a Sound object in Wwise. It indicates
        that the real sound data will be provided at run time. While External Source conversion is also
        triggered by SoundBank generation, this operation can be used to process sources not contained in
        the Wwise Project. Please refer to Wwise SDK help page "Integrating External Sources".
        :param sources: An array of external sources files and corresponding arguments. Duplicates are ignored.
        :return: Whether the call succeeded.
        """
        args = {"sources": [source.dictionary for source in sources]}
        return self._client.call("ak.wwise.core.soundbank.convertExternalSources", args) is not None
    
    def generate(self, sound_banks: ListOrTuple[SoundBankInfo] = None, platforms: ListOrTuple[GUID | Name] = None,
                 languages: ListOrTuple[GUID | Name] = None, clear_audio_file_cache: bool = False,
                 write_to_disk: bool = False, rebuild_init_bank: bool = False) -> dict:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_soundbank_generate.html \n
        Generate a list of SoundBanks with the import definition specified in the WAAPI request. If you
        do not write the SoundBanks to disk, subscribe to `ak.wwise.core.soundbank.generated` to receive
        SoundBank structure info and the bank data as base64. Note: This is a synchronous operation.
        :param sound_banks: A list of SoundBanks to generate.
        :param platforms: A list of platforms to generate. By default, all platforms will be generated.
        :param languages: A list of languages to generate. By default, all languages will be generated. To skip
                          languages, pass an empty set (`set()`) as the argument.
        :param clear_audio_file_cache: Deletes the content of the Wwise audio file cache folder prior to converting
                                       source files and generating SoundBanks, which ensures that all source files are
                                       reconverted.
        :param write_to_disk: Will write the sound bank and info file to disk.
        :param rebuild_init_bank: Use this option to force a rebuild of the Init bank for each specified platform.
        :return: The SoundBank generation log, as a dictionary. An empty dictionary means the log could not be
                  retrieved.
        """
        # Remove duplicates in collections
        sound_banks = list(dict.fromkeys(sound_banks)) if sound_banks is not None else list[SoundBankInfo]()
        platforms = list(dict.fromkeys(platforms)) if platforms is not None else list[GUID | Name]()
        languages = list(dict.fromkeys(languages)) if languages is not None else list[GUID | Name]()
        
        args = dict()
        
        if sound_banks:  # if valid and not empty
            args["soundbanks"] = [{"name": sound_bank} for sound_bank in sound_banks]
        else:
            args["rebuildSoundBanks"] = True
        
        if platforms:  # None = all platforms; no need to handle that here.
            args["platforms"] = platforms
        
        if languages:  # None = all languages; no need to handle that here.
            args["languages"] = languages
        else:  # no languages; user explicitly passed an empty set
            args["skipLanguages"] = True
        
        args["clearAudioFileCache"] = clear_audio_file_cache
        args["writeToDisk"] = write_to_disk
        args["rebuildInitBank"] = rebuild_init_bank
        
        log = self._client.call("ak.wwise.core.soundbank.generate", args).get("logs")
        return log if log is not None else dict()
    
    def get_inclusions(self, sound_bank: GUID | Name | ProjectPath) -> tuple[SoundBankInclusion, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_soundbank_getinclusions.html \n
        Retrieves a SoundBank's inclusion list.
        :param sound_bank: The GUID, name, or project path of the SoundBank to get inclusions from.
        :return: An array of SoundBank inclusions.
        """
        if isinstance(sound_bank, Name):
            sound_bank = f"{EObjectType.SOUND_BANK.get_type_name()}:{sound_bank}"
        
        args = {"soundbank": sound_bank}
        results = self._client.call("ak.wwise.core.soundbank.getInclusions", args)
        
        if results is None:
            return tuple[SoundBankInclusion, ...]()
        
        results = results.get("inclusions", ())
        
        if not results:  # Empty.
            return tuple[SoundBankInclusion, ...]()
        
        inclusions = list[SoundBankInclusion]()
        
        for result in results:
            obj: GUID = GUID(result.get("object", GUID.get_null()))
            filters = tuple([EnumStatics.from_value(EInclusionFilter, _filter) for _filter in result.get("filter", ())])
            inclusions.append(SoundBankInclusion(obj, filters))
        
        return tuple[SoundBankInclusion, ...](inclusions)
    
    def process_definition_files(self, files: ListOrTuple[SystemPath]) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_soundbank_processdefinitionfiles.html \n
        Imports SoundBank definitions from the specified file. Multiple files can be specified. See the
        WAAPI log for status messages.
        :param files: An array of SoundBank definition files.
        :return: Whether the call succeeded.
        """
        args = {"files": [str(file) for file in list(dict.fromkeys(files))]}  # File paths should be unique.
        return self._client.call("ak.wwise.core.soundbank.processDefinitionFiles", args) is not None
    
    def set_inclusions(self, sound_bank: Name | GUID | ProjectPath, operation: EInclusionOperation,
                       inclusions: ListOrTuple[SoundBankInclusion]) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_soundbank_setinclusions.html \n
        Modifies a SoundBank's inclusion list. The 'operation' argument determines how the 'inclusions'
        argument modifies the SoundBank's inclusion list; 'inclusions' may be added to / removed from /
        replace the SoundBank's inclusion list.
        :param sound_bank: The GUID, name, or project path of the SoundBank to add an inclusion to.
        :param operation: Determines how the 'inclusions' argument is used to modify the SoundBank's inclusion list.
        :param inclusions: An array of SoundBank inclusions.
        :return: Whether the call succeeded.
        """
        if isinstance(sound_bank, Name):
            sound_bank = f"{EObjectType.SOUND_BANK.get_type_name()}:{sound_bank}"
        args = {"soundbank": sound_bank, "operation": operation,
                "inclusions": [inclusion.dictionary for inclusion in list(dict.fromkeys(inclusions))]}
        return self._client.call("ak.wwise.core.soundbank.setInclusions", args) is not None
