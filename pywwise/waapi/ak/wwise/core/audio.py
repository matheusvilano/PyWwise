# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient
from simplevent import RefEvent as _RefEvent
from pywwise.aliases import SystemPath, ListOrTuple
from pywwise.decorators import callback
from pywwise.enums import EReturnOptions, EObjectType, EAudioImportOperation, EBasePlatform, EImportOperation
from pywwise.enums import ELogSeverity, EReturnOptions, EObjectType, EImportOperation
from pywwise.primitives import Name, GUID, ProjectPath
from pywwise.statics import EnumStatics
from pywwise.structs import DPlatformInfo, WwiseObjectInfo, DAudioImportEntry
from pywwise.structs import AudioImportEntry, ConversionLogItem, WwiseObjectInfo


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
        event(EnumStatics.from_value(EAudioImportOperation, kwargs["operation"]), tuple(objects),
              tuple([SystemPath(file) for file in kwargs.get("files", ())]))

    def convert(self, objects: ListOrTuple[GUID | Name | ProjectPath], platforms: ListOrTuple[GUID | Name],
                languages: ListOrTuple[Name]) -> tuple[ConversionLogItem, ...]:
        """
        https://www.audiokinetic.com/en/library/2024.1.0_8598/?source=SDK&id=ak_wwise_core_audio_convert.html \n
        Creates converted audio files. When errors occur, this function returns a list of messages with corresponding
        levels of severity. The converted audio files are located within the ".cache" folder in the Wwise project
        root folder.
        :param objects: An array of object GUIDs, unique Names, or Project Paths.
        :param platforms: An array of platform GUIDs or unique Names.
        :param languages: An array of language unique Names.
        :return: A tuple of logged entries with associated messages and severities. If empty, the conversion(s) worked
                 without any errors, warnings, etc.
        """
        args = {"objects": objects, "platforms": platforms, "languages": languages}
        result: dict[str, list[dict[str, str]]] = self._client.call("ak.wwise.core.audio.convert", args)
        return tuple(ConversionLogItem(EnumStatics.from_value(ELogSeverity, error["severity"]),
                                       error.get("message", "")) for error in result.get("errors", ()))

    # "import" is a reserved keyword, so function name does not match that of WAAPI
    def import_files(self, default_import_properties: DAudioImportEntry,
                     additional_import_properties: ListOrTuple[DAudioImportEntry],
                     import_operation: EAudioImportOperation = EAudioImportOperation.USE_EXISTING,
                     auto_add_to_version_control: bool = True, auto_checkout_to_version_control: bool = True,
                     return_options: ListOrTuple[EReturnOptions] = None, platform: DPlatformInfo | Name | GUID = None,
                     language: str | GUID = None):
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_audio_import.html \n
        Creates Wwise objects and imports audio files. This function does not return an error when
        something fails during the import process, please refer to the log for the result of each import
        command. This function uses the same importation processor available through the Tab Delimited
        import in the Audio File Importer. The function returns an array of all objects created,
        replaced or re-used. Use the options to specify how the objects are returned. For more
        information, refer to Importing Audio Files and Creating Structures.
        :param default_import_properties: Default values for each item in "imports". Use this object to avoid repeating
                                          common properties of every imported element.
        :param additional_import_properties: An audio import entry. The members of this object are combined with those
                                             of "default", with this object's members having precedence.
        :param import_operation: Determines how import object creation is performed. Make use of EImportOperation to
                                 select the desired import operation.
        :param auto_add_to_version_control: Determines if Wwise automatically performs a source control Add operation on
                                            the imported files. Defaults to true.
        :param auto_checkout_to_version_control: Determines if Wwise automatically performs a source control Checkout
                                                 operation (when applicable) on the modified files. Defaults to true.
        :param return_options: The list of return expressions defines which elements of the Wwise object is returned.
                               This can include built-in accessors, such as the name or id, or object properties, such
                               as the Volume or the Pitch. This is an optional argument.
        :param platform: Determines what platform the Wwise object is returned. This is an optional argument. When not
                         specified, the current platform is used.
        :param language: Determines the language to be used.
        """
        args = {"importOperation": import_operation, "autoAddToSourceControl": auto_add_to_version_control,
                "autoCheckOutToSourceControl": auto_checkout_to_version_control}
        
        if default_import_properties is not None:
            args["default"] = {"importLanguage": default_import_properties.import_language,
                               "importLocation": default_import_properties.import_location,
                               "audioFile": default_import_properties.audio_file,
                               "audioFileBase64": default_import_properties.audio_file_base64,
                               "originalsSubFolder": default_import_properties.originals_sub_folder,
                               "objectPath": default_import_properties.object_path,
                               "objectType": default_import_properties.object_type,
                               "notes": default_import_properties.notes,
                               "audioSourceNotes": default_import_properties.audio_source_notes,
                               "switchAssignation": default_import_properties.switch_assignation,
                               "event": default_import_properties.event,
                               "dialogueEvent": default_import_properties.dialogue_event,
                               "regex(^@[:_a-zA-Z0-9]+$)": default_import_properties.regex}
        
        if additional_import_properties is not None:
            args["additionalImportProperties"] = list()
            for import_property in additional_import_properties:
            
            
        
        returns = list(dict.fromkeys(return_options)) if return_options is not None else list[EReturnOptions]()
        returns.extend(EReturnOptions.get_defaults())
        options = {"return": returns}
        
        if platform is not None:
            options["platform"] = platform
        if language is not None:
            options["language"] = language
        
        self._client.call("ak.wwise.core.audio.import", args, options=options)

    def import_tab_delimited(self, tsv_file: SystemPath, operation: EImportOperation, language: Name = Name("SFX"),
                             location: GUID | tuple[EObjectType, Name] | ProjectPath = None,
                             auto_add_to_version_control: bool = True, auto_checkout_to_version_control: bool = True,
                             returns: [EReturnOptions] = None) -> tuple[WwiseObjectInfo, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_audio_importtabdelimited.html \n
        Scripted object creation and audio file import from a tab-delimited file.
        """
        raise NotImplementedError()

    def mute(self, objs: ListOrTuple[GUID | tuple[EObjectType, Name] | ProjectPath], value: bool) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_audio_mute.html \n
        Mute or unmute objects.
        :param objs: The GUID, Name, or Project Path of the objects to mute. Using Names is supported for object
        types that have unique names (e.g. Buses, Events, etc.), but it is still NOT recommended. If you choose to use
        Names, you will have to specify the type of the object (e.g. `Name("Event:Play_Footstep")`).
        :param value: Whether the objects should be muted or not.
        :return: Whether the call succeeded. True does not necessarily mean objects were muted/unmuted successfully.
        """
        objs = [obj if not isinstance(obj, tuple) else f"{obj[0].get_type_name()}:{obj[1]}" for obj in objs]
        args = {"objects": objs, "value": value}
        return self._client.call("ak.wwise.core.audio.mute", args) is not None

    def reset_mute(self) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_audio_resetmute.html \n
        Unmute all muted objects.
        :return: Whether the call succeeded. True does not necessarily mean objects were unmuted successfully.
        """
        return self._client.call("ak.wwise.core.audio.resetMute") is not None

    def reset_solo(self) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_audio_resetsolo.html \n
        Unsolo all soloed objects.
        :return: Whether the call succeeded. True does not necessarily mean objects were unsoloed successfully.
        """
        return self._client.call("ak.wwise.core.audio.resetSolo") is not None

    def set_conversion_plugin(self, conversion: GUID | Name | ProjectPath, plugin: Name, platform: GUID | Name) -> bool:
        """
        https://www.audiokinetic.com/en/library/2024.1.0_8598/?source=SDK&id=ak_wwise_core_audio_setconversionplugin.html \n
        :param conversion: The GUID, Name, or Project Path or a Conversion shareset.
        :param plugin: The name of the plugin to use for future conversions (e.g. Vorbis).
        :param platform: The GUID or Name of the platform to which the settings apply.
        :return: Whether the call succeeded.
        """
        conversion = conversion if not isinstance(conversion, Name) else f"{EObjectType.CONVERSION}:{conversion}"
        args = {"conversion": conversion, "plugin": plugin, "platform": platform}
        return self._client.call("ak.wwise.core.audio.setConversionPlugin", args) is not None

    def solo(self, objs: ListOrTuple[GUID | tuple[EObjectType, Name] | ProjectPath], value: bool) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_audio_solo.html \n
        Solos an object.
        :param objs: The GUIDs, typed names, or project paths of the objects to solo. Using names is supported only for
                     object types that have unique names (e.g. Buses, Events, etc.), but it is still NOT recommended.
        :param value: Whether the object is soloed or not. 1 is true, 0 is false.
        :return: Whether the call succeeded. True does not necessarily mean objects were soloed/unsoloed successfully.
        """
        objs = [obj if not isinstance(obj, tuple) else f"{obj[0].get_type_name()}:{obj[1]}" for obj in objs]
        args = {"objects": objs, "value": value}
        return self._client.call("ak.wwise.core.audio.solo", args) is not None
