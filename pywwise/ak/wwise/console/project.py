from pathlib import Path as _Path
from waapi import WaapiClient as _WaapiClient
from pywwise.enums import EBasePlatform as _EBasePlatform
from pywwise.structs import PlatformInfo as _PlatformInfo


class Project:
	"""ak.wwise.console.project"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
	
	def close(self) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_console_project_close.html \n
		Closes the current project. This operation is synchronous.
		:return: True if there was a project open and it closed successfully; otherwise, false.
		"""
		results = self._client.call("ak.wwise.console.project.close")
		return results.get("hadProjectOpen", False) if results is not None else False
	
	def create(self, project_path: _Path,
	           platforms: set[_PlatformInfo] = (_PlatformInfo("Windows", _EBasePlatform.WINDOWS),),
	           languages: tuple[str, ...] = tuple("English(US)")) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_console_project_create.html \n
		Creates, saves and opens new empty project, specified by path and platform. The project has no
		factory setting WorkUnit. This operation is synchronous.
		:param project_path: The path to the project WPROJ file. Example: "C:/Projects/MyProject/MyProject.wproj".
		:param platforms: Specifies the platform(s) supported by the new project. If not specified, only Windows is used.
		:param languages: Array of languages to creates for this project. If not specified, English(US) becomes the
		default language. When multiple languages are specified, the first one becomes the default language.
		:return: Whether the call succeeded. True does not necessarily mean the project was successfully created.
		"""
		args = {"path": str(project_path), "platforms": list(), "languages": [language for language in languages]}
		for platform in platforms:
			args["platforms"].append({"name": platform.name, "basePlatform": platform.base_platform})
		return self._client.call("ak.wwise.console.project.create", args) is not None
	
	def open(self, project_path: _Path, is_migration_allowed: bool, auto_checkout: bool) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_console_project_open.html \n
		Opens a project, specified by path. This operation is synchronous.
		:param project_path: The path to the project WPROJ file.
		:param is_migration_allowed: Whether migration is allowed.
		:param auto_checkout: Determines if Wwise automatically performs a Checkout source control
		operation for affected work units and for the project. Defaults to true.
		:return: Whether the call succeeded. True does not necessarily mean the project was successfully opened.
		"""
		migration_action = "migrate" if is_migration_allowed else "fail"
		args = {"path": str(project_path), "onMigrationRequired": migration_action, "autoCheckOutToSourceControl": auto_checkout}
		return self._client.call("ak.wwise.console.project.open", args) is not None
		
