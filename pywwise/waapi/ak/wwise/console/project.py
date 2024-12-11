# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient

from pywwise.aliases import ListOrTuple, SystemPath
from pywwise.decorators import console_instance_only
from pywwise.enums import EBasePlatform
from pywwise.primitives import Name
from pywwise.structs import PlatformInfo


class Project:
    """ak.wwise.console.project"""
    
    def __init__(self, client: _WaapiClient, is_console_instance: bool = False):
        """
        Constructor.
        :param client: The WAAPI client to use.
        :param is_console_instance: Should be set to true if the instance of Wwise is running in a console window.
        """
        self._client = client
        self._is_console_instance = is_console_instance
    
    @console_instance_only
    def close(self) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_console_project_close.html \n
        Closes the current project. This operation is synchronous.
        :return: True if there was a project open and it closed successfully; otherwise, false.
        """
        results = self._client.call("ak.wwise.console.project.close")
        return results.get("hadProjectOpen", False) if results is not None else False
    
    @console_instance_only
    def create(self, project_path: SystemPath,
               platforms: ListOrTuple[PlatformInfo] = (PlatformInfo("Windows", EBasePlatform.WINDOWS),),
               languages: ListOrTuple[Name] = tuple(Name("English(US)"))) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_console_project_create.html \n
        Creates, saves and opens new empty project, specified by path and platform. The project has no
        factory setting WorkUnit. This operation is synchronous.
        :param project_path: The path to the project WPROJ file. Example: "C:/Projects/MyProject/MyProject.wproj".
        :param platforms: Specifies the platform(s) supported by the new project. If not specified, only Windows is
                          used.
        :param languages: Array of languages to creates for this project. If not specified, English(US) becomes the
                          default language. When multiple languages are specified, the first one becomes the default
                          language.
        :return: Whether the call succeeded. True does not necessarily mean the project was successfully created.
        """
        platforms = list(dict.fromkeys(platforms))
        args = {"path": str(project_path), "platforms": list(), "languages": [language for language in languages]}
        for platform in platforms:
            args["platforms"].append({"name": platform.name, "basePlatform": platform.base})
        return self._client.call("ak.wwise.console.project.create", args) is not None
    
    @console_instance_only
    def open(self, project_path: SystemPath,
             is_migration_allowed: bool,
             version_control_auto_checkout: bool = True) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_console_project_open.html \n
        Opens a project, specified by path. This operation is synchronous.
        :param project_path: The path to the project WPROJ file.
        :param is_migration_allowed: Whether migration is allowed.
        :param version_control_auto_checkout: Determines if Wwise automatically performs a Checkout source control
                                              operation for affected work units and for the project. Only supported in
                                              Wwise 2023 or above.
        :return: Whether the call succeeded. True does not necessarily mean the project was successfully opened.
        """
        migration_action = "migrate" if is_migration_allowed else "fail"
        args = {"path": str(project_path),
                "onMigrationRequired": migration_action,
                **({"autoCheckOutToSourceControl": False} if not version_control_auto_checkout else {})}
        return self._client.call("ak.wwise.console.project.open", args) is not None
