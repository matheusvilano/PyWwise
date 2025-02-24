# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from typing import Any as _Any

from waapi import WaapiClient as _WaapiClient

from pywwise.aliases import ListOrTuple, SystemPath
from pywwise.enums import EBasePlatform, EObjectType, EReturnOptions, EWwiseBuildConfiguration, EWwiseBuildPlatform
from pywwise.primitives import GUID, Name, ProjectPath
from pywwise.statics import EnumStatics
from pywwise.structs import (LanguageInfo, PlatformInfo, WwiseGlobalDirectories, WwiseGlobalInfo, WwiseObjectInfo,
                             WwiseObjectWatch, WwiseProjectInfo, WwiseVersionInfo)
from pywwise.waapi.ak.wwise.core.audio import Audio as _Audio
from pywwise.waapi.ak.wwise.core.audio_source_peaks import AudioSourcePeaks as _AudioSourcePeaks
from pywwise.waapi.ak.wwise.core.log import Log as _Log
from pywwise.waapi.ak.wwise.core.object import Object as _Object
from pywwise.waapi.ak.wwise.core.profiler import Profiler as _Profiler
from pywwise.waapi.ak.wwise.core.project import Project as _Project
from pywwise.waapi.ak.wwise.core.remote import Remote as _Remote
from pywwise.waapi.ak.wwise.core.sound import Sound as _Sound
from pywwise.waapi.ak.wwise.core.soundbank import SoundBank as _SoundBank
from pywwise.waapi.ak.wwise.core.source_control import SourceControl as _SourceControl
from pywwise.waapi.ak.wwise.core.switch_container import SwitchContainer as _SwitchContainer
from pywwise.waapi.ak.wwise.core.transport import Transport as _Transport
from pywwise.waapi.ak.wwise.core.undo import Undo as _Undo


class Core:
    """ak.wwise.core"""
    
    def __init__(self, client: _WaapiClient, watch_list: tuple[WwiseObjectWatch, ...] = ()):
        """
        Constructor.
        :param client: The WAAPI client to use.
        :param watch_list: A tuple of `WwiseObjectWatch` instances. This will be used to set up the
                           `ak.wwise.core.object.property_changed` event.
        """
        self._client = client
        self.audio = _Audio(client)
        self.audio_source_peaks = _AudioSourcePeaks(client)
        self.log = _Log(client)
        self.object = _Object(client, watch_list)
        self.profiler = _Profiler(client)
        self.project = _Project(client)
        self.remote = _Remote(client)
        self.sound = _Sound(client)
        self.soundbank = _SoundBank(client)
        self.source_control = _SourceControl(client)
        self.switch_container = _SwitchContainer(client)
        self.transport = _Transport(client)
        self.undo = _Undo(client)
    
    def execute_lua_script(self, lua_script: SystemPath,
                           lua_paths: ListOrTuple[SystemPath] = (),
                           requires: ListOrTuple[str] = (),
                           do_files: ListOrTuple[SystemPath] = ()) -> _Any | None:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_executeluascript.html \n
        Execute a Lua script. Optionally, specify additional Lua search paths, additional modules, and additional Lua
        scripts to load prior to the main script. The script can return a value. All arguments will be passed to the
        Lua script in the "wa_args" global variable.
        :param lua_script: The Lua script to load and execute.
        :param lua_paths: An array of paths to be used to search additional Lua modules.
        :param requires: An array of additional modules to be loaded at runtime using the `require` system in Lua. Note
                         that the following folders are automatically added in the Lua path: "PROJECT/Add-ons/Lua",
                         "APPDATA/Audiokinetic/Wwise/Add-ons/Lua", and "INSTALLDIR/Authoring/Data/Add-ons/Lua".
        :param do_files: An array of additional Lua files to load before the main Lua script is loaded and executed. It
                         is also possible to specify a directory in which all Lua files will be loaded.
        :return: Result returned by the Lua script. Use a return statement at the end of the Lua script.
        """
        args = {"luaScript": str(lua_script), "luaPaths": [str(path) for path in lua_paths],
                "requires": requires, "doFiles": [str(file) for file in do_files]}
        result = self._client.call("ak.wwise.core.executeLuaScript", args)
        return result.get("return", None) if result is not None else None
    
    def get_info(self) -> WwiseGlobalInfo:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_getinfo.html \n
        Retrieve global Wwise information.
        :return: A WwiseGlobalInfo object containing information about Wwise (e.g. version, platform, etc.).
        """
        info = self._client.call("ak.wwise.core.getInfo")
        
        version = info["version"]
        version = WwiseVersionInfo(version["displayName"], version["year"], version["major"], version["minor"],
                                   version["build"], version["nickname"], version["schema"])
        
        config = EnumStatics.from_value(EWwiseBuildConfiguration, info["configuration"])
        
        platform = EnumStatics.from_value(EWwiseBuildPlatform, info["platform"])
        
        dirs = info["directories"]
        dirs = WwiseGlobalDirectories(SystemPath(dirs["install"]), SystemPath(dirs["authoring"]),
                                      SystemPath(dirs["bin"]), SystemPath(dirs["help"]), SystemPath(dirs["user"]))
        
        return WwiseGlobalInfo(session_id=GUID(info["sessionId"]),
                               api_version=float(info["apiVersion"]),
                               display_name=info["displayName"],
                               branch=info["branch"],
                               version=version,
                               configuration=config,
                               platform=platform,
                               is_command_line=info["isCommandLine"],
                               process_id=info["processId"],
                               process_path=info["processPath"],
                               directories=dirs,
                               copyright_info=info["copyright"])
    
    def get_project_info(self) -> WwiseProjectInfo:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_getprojectinfo.html \n
        Retrieve information about the current project opened, including platforms, languages and project directories.
        :return: A WwiseProjectInfo instance containing information about a Wwise project.
        """
        info = self._client.call("ak.wwise.core.getProjectInfo")
        
        name = Name(info.get("name", Name.get_null()))
        display_title = info.get("displayTitle", "")
        path = SystemPath(info.get("path", ""))
        guid = GUID(info.get("id", GUID.get_null()))
        is_dirty = info.get("isDirty", False)
        current_language_id = GUID(info.get("currentLanguageId", GUID.get_null()))
        reference_language_id = GUID(info.get("referenceLanguageId", GUID.get_null()))
        current_platform_id = GUID(info.get("currentPlatformId", GUID.get_null()))
        
        languages = tuple([LanguageInfo(guid=lang["id"], name=lang["name"], short_id=lang["shortId"])
                           for lang in info["languages"]])
        
        platforms = tuple([PlatformInfo(name=plat["name"], base=EnumStatics.from_value(EBasePlatform, plat["baseName"]),
                                        guid=plat["id"], sound_bank_path=SystemPath(plat["soundBankPath"]),
                                        copied_media_path=plat["copiedMediaPath"])
                           for plat in info["platforms"]])
        
        conversion = info["defaultConversion"]["id"]
        conversion = self._client.call("ak.wwise.core.object.get",  # We need this call here to get the ProjectPath.
                                       {"waql": f"$ from object \"{conversion}\""},  # It will always return 1 item.
                                       options={"return": EReturnOptions.get_defaults()})["return"][0]
        conversion = WwiseObjectInfo(GUID(conversion["id"]), Name(conversion["name"]),
                                     EObjectType.CONVERSION, ProjectPath(conversion["path"]))
        
        return WwiseProjectInfo(name, display_title, path, guid, is_dirty, current_language_id, reference_language_id,
                                current_platform_id, languages, platforms, conversion)
    
    def ping(self) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_ping.html \n
        Verify if WAAPI is currently available.
        :return: `True` if WAAPI is available. Note that WAAPI is not available when a modal dialog is shown.
        """
        result = self._client.call("ak.wwise.core.ping")
        return False if result is None else result.get("isAvailable", False)
