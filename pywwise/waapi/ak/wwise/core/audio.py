# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient
from simplevent import RefEvent as _RefEvent
from pywwise.aliases import SystemPath, ListOrTuple
from pywwise.decorators import callback
from pywwise.enums import ELogSeverity, EReturnOptions, EObjectType, EImportOperation
from pywwise.primitives import Name, GUID, ProjectPath
from pywwise.statics import EnumStatics
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
        event(EnumStatics.from_value(EImportOperation, kwargs["operation"]), tuple(objects),
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
    def import_files(self, imports: ListOrTuple[AudioImportEntry], operation: EImportOperation):
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_audio_import.html \n
        Creates Wwise objects and imports audio files. This function does not return an error when something fails
        during the import process, please refer to the log for the result of each import command. This function uses
        the same importation processor available through the Tab Delimited import in the Audio File Importer. The
        function returns an array of all objects created, replaced or re-used. Use the options to specify how the
        objects are returned. For more information, refer to Importing Audio Files and Creating Structures.
        """
        raise NotImplementedError()

    def import_tab_delimited(self, tsv_file: SystemPath, operation: EImportOperation, language: Name = Name("SFX"),
                             location: GUID | tuple[EObjectType, Name] | ProjectPath = None,
                             auto_add_to_version_control: bool = True, auto_checkout_to_version_control: bool = True,
                             returns: EReturnOptions = None) -> tuple[WwiseObjectInfo, ...]:
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
