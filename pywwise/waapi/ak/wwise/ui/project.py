# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient

from pywwise.aliases import SystemPath
from pywwise.structs import PlatformInfo


class Project:
    """ak.wwise.ui.project"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
    
    def close(self, bypass_save: bool = True) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_ui_project_close.html \n
        Closes the current project.
        :param bypass_save: Indicates if the user should not be prompted to save the current project.
                            **Defaults to true.**
        :return: True if there was a project open, false otherwise. Note that if there was no project open,
                 no `ak.wwise.core.project.pre_closed` or `ak.wwise.core.project.post_closed` event is issued.
        """
        args = {"bypassSave": bypass_save}
        result = self._client.call("ak.wwise.ui.project.close", args)
        return result.get("hadProjectOpen")
    
    def create(self, path: SystemPath, platforms: set[PlatformInfo] = None, languages: set[str] = None) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_ui_project_create.html \n
        Creates, saves and opens new empty project, specified by path and platform. The project has no
        factory setting WorkUnit. Please refer to `ak.wwise.core.project.loaded` for further explanations
        on how to be notified when the operation has completed.
        :param path: The path to the project WPROJ file. The path must use the same name for the WPROJ and the parent
                     directory folder. For example: `C:/PyWwise/Projects/MYPROJECT/MYPROJECT.wproj`.
        :param platforms: Specifies the platform or platforms supported by the new project. If not specified, only
                          Windows is used. Duplicates are not allowed; platforms should have **unique names**.
        :param languages: Array of languages to creates for this project. If not specified, the English(US) language is
                          created. When multiple languages are specified, the first one becomes the default language.
        :return: Whether the project creation succeeded. This is done by checking if the specified path now
                 exists.
        """
        args = {"path": str(path)}
        
        if platforms is not None:
            args["platforms"] = list()
            for platform in platforms:
                args["platforms"].append({"name": platform.name, "basePlatform": platform.base})
        if languages is not None:
            args["languages"] = list(languages)
        
        self._client.call("ak.wwise.ui.project.create", args)
        return path.exists()
    
    def open(self, path: SystemPath, is_migration_required: bool = False, bypass_save: bool = True,
             version_control_auto_checkout: bool = True) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_ui_project_open.html \n
        Opens a project, specified by path. Please refer to `ak.wwise.core.project.loaded` for further
        explanations on how to be notified when the operation has completed.
        :param path: The path to the project WPROJ file. For using WAAPI on Mac, please refer to Using WAAPI on Mac.
        :param is_migration_required: Whether migration is required or not.
        :param bypass_save: Indicates if the user should not be prompted to save the current project.
        :param version_control_auto_checkout: Determines if Wwise automatically performs a Checkout source control
                                              operation for affected work units and for the project. Only supported
                                              in Wwise 2023 or above.
        :return: Returns whether the project was open.
        """
        if not path.exists():
            return False
        
        migration_action = "migrate" if is_migration_required else "fail"
        
        args = {"path": str(path),
                "onMigrationRequired": migration_action,
                "bypassSave": bypass_save,
                **({"autoCheckoutToSourceControl": False} if not version_control_auto_checkout else {})}
        
        return self._client.call("ak.wwise.ui.project.open", args) is not None
