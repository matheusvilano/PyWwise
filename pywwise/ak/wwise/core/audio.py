# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient
from simplevent import RefEvent as _RefEvent
from pywwise.aliases import SystemPath, ListOrTuple
from pywwise.decorators import callback
from pywwise.enums import EReturnOptions, EObjectType, EImportOperation
from pywwise.primitives import Name, GUID, ProjectPath
from pywwise.statics import EnumStatics
from pywwise.structs import WwiseObjectInfo, AudioImportEntry


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

    # "import" is a reserved keyword, so function name does not match that of WAAPI
    def import_files(self, imports: ListOrTuple[AudioImportEntry], operation: EImportOperation):
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_audio_import.html \n
        Creates Wwise objects and imports audio files. This function does not return an error when
        something fails during the import process, please refer to the log for the result of each import
        command. This function uses the same importation processor available through the Tab Delimited
        import in the Audio File Importer. The function returns an array of all objects created,
        replaced or re-used. Use the options to specify how the objects are returned. For more
        information, refer to Importing Audio Files and Creating Structures.
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
