# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient

from pywwise.aliases import ListOrTuple, SystemPath
from pywwise.enums import EReturnOptions, ESourceControlSearchFilter, ESourceFileReturnOptions
from pywwise.primitives import OriginalsPath
from pywwise.structs import LogItem, SourceControlStatus, SourceFileInfo, WwiseObjectInfo


class SourceControl:
    """ak.wwise.core.sourceControl"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
    
    def add(self, files: ListOrTuple[SystemPath]) -> tuple[LogItem, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_sourcecontrol_add.html \n
        Add files to source control. Equivalent to Mark for Add for Perforce.
        :param files: Array of files to add. File paths must be absolute.
        :return: A tuple containing log items generating during the request.
        """
        files = list(dict.fromkeys(files))  # convert to list of unique items
        result = self._client.call("ak.wwise.core.sourceControl.add", {"files": files})
        return tuple([LogItem.from_dict(result["log"])] if result is not None else [])
    
    def check_out(self, files: ListOrTuple[SystemPath]) -> tuple[LogItem, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_sourcecontrol_checkout.html \n
        Check out files from source control. Equivalent to Check Out for Perforce.
        :param files: Array of files to check out. File paths must be absolute.
        :return: A tuple containing log items generating during the request.
        """
        files = list(dict.fromkeys(files))  # convert to list of unique items
        result = self._client.call("ak.wwise.core.sourceControl.checkOut", {"files": files})
        return tuple([LogItem.from_dict(result["log"])] if result is not None else [])
    
    def commit(self, files: ListOrTuple[SystemPath], message: str) -> tuple[LogItem, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_sourcecontrol_commit.html \n
        Commit files to source control. Equivalent to Submit Changes for Perforce.
        :param files: Array of files to commit. File paths must be absolute.
        :param message: Description message for the commit.
        :return: A tuple containing log items generating during the request.
        """
        files = list(dict.fromkeys(files))  # convert to list of unique items
        result = self._client.call("ak.wwise.core.sourceControl.commit", {"files": files, "message": message})
        return tuple([LogItem.from_dict(result["log"])] if result is not None else [])
    
    def delete(self, files: ListOrTuple[SystemPath]) -> tuple[LogItem, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_sourcecontrol_delete.html \n
        Delete files from source control. Equivalent to Mark for Delete for Perforce.
        :param files: Array of files to delete. File paths must be absolute.
        :return: A tuple containing log items generating during the request.
        """
        files = list(dict.fromkeys(files))  # convert to list of unique items
        result = self._client.call("ak.wwise.core.sourceControl.delete", {"files": files})
        return tuple([LogItem.from_dict(result["log"])] if result is not None else [])
    
    def get_source_files(self, folder: str = None, recursive: bool = True,
                         search_filter: ESourceControlSearchFilter = ESourceControlSearchFilter.ALL) -> tuple[
        SourceFileInfo, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_sourcecontrol_getsourcefiles.html \n
        Retrieve all original files.
        :param folder: Base folder for search relative to Originals folder. Default to the Originals folder.
        :param recursive: Search in all subfolders of the base folder.
        :param search_filter: Filter the files are in the search result.
        :return: A tuple containing SourceFileInfo instances, which represent information on each source file found.
                 Empty is no files were found.
        """
        args = {"recursive": recursive, "filter": search_filter}
        if folder is not None:
            args["folder"] = folder
        
        options = {"return": [ESourceFileReturnOptions.FILE, ESourceFileReturnOptions.USAGE,
                              ESourceFileReturnOptions.IS_MISSING],
                   "objectReturn": EReturnOptions.get_defaults()}
        
        results = self._client.call("ak.wwise.core.sourceControl.getSourceFiles", args, options=options)
        if results is None:
            return ()
        
        returns = list[SourceFileInfo]()
        for result in results.get("return", ()):
            file = OriginalsPath(result["file"])
            usage = tuple([WwiseObjectInfo.from_dict(obj) for obj in result.get("usage", ())])
            is_missing = result["isMissing"]
            returns.append(SourceFileInfo(file, usage, is_missing))
        return tuple(returns)
    
    def get_status(self, files: ListOrTuple[tuple[SystemPath, SystemPath]]) -> tuple[
        tuple[LogItem, ...], tuple[SourceControlStatus, ...]]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_sourcecontrol_getstatus.html \n
        Get the source control status of the specified files.
        :param files: Array of files for which to retrieve source control status. File paths must be absolute.
        :return: Two tuples: the first one containing log items generating during the request; the second one
                 containing the source control status for each file passed to `files`.
        """
        files = list(dict.fromkeys(files))  # convert to list of unique items
        result = self._client.call("ak.wwise.core.sourceControl.delete", {"files": files})
        if result is None:
            return (), ()
        logs = tuple([LogItem.from_dict(result["log"])])
        statuses = tuple([SourceControlStatus(result.get("result", dict()).get("status", ""),
                                              result.get("result", dict()).get("owner", ""))])
        return logs, statuses
    
    def move(self, files: ListOrTuple[tuple[SystemPath, SystemPath]]) -> tuple[LogItem, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_sourcecontrol_move.html \n
        Move or rename files in source control. Always pass the same number of elements in files and
        newFiles. Equivalent to Move for Perforce.
        :param files: Array of files to move. File paths must be absolute.
        :return: A tuple containing log items generating during the request.
        """
        original_paths, new_paths = zip(*files)
        args = {"files": original_paths, "newFiles": new_paths}
        result = self._client.call("ak.wwise.core.sourceControl.move", args)
        return tuple([LogItem.from_dict(result["log"])] if result is not None else [])
    
    def revert(self, files: ListOrTuple[SystemPath]) -> tuple[LogItem, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_sourcecontrol_revert.html \n
        Revert changes to files in source control.
        :param files: Array of files to revert. File paths must be absolute.
        :return: A tuple containing log items generating during the request.
        """
        files = list(dict.fromkeys(files))  # convert to list of unique items
        result = self._client.call("ak.wwise.core.sourceControl.revert", {"files": files})
        return tuple([LogItem.from_dict(result["log"])] if result is not None else [])
    
    def set_provider(self, provider: str, server: str = "localhost", port: str = "", username: str = "",
                     password: str = "", workspace: str = "", host: str = "") -> tuple[LogItem, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_sourcecontrol_setprovider.html \n
        Change the source control provider and credentials. This is the same setting as the Source
        Control option in the Project Settings dialog in Wwise.
        :param provider: Source control provider. Allowed values "Perforce", "Subversion", any other source control
                         supported or an empty string. An empty value is the equivalent of choosing No Control Source
                         in the UI.
        :param server: Server name or address. Default value is localhost.
        :param port: Server port. This value is required for Perforce.
        :param username: Username. This value is required for Perforce.
        :param password: User password or ticket. This value is required for Perforce.
        :param workspace: Workspace name. This value is required for Perforce.
        :param host: Host name. This value is required for Perforce.
        :return: A tuple containing log items generating during the request.
        """
        args = {"provider": provider, "server": server, "port": port, "username": username, "password": password,
                "workspace": workspace, "host": host}
        result = self._client.call("ak.wwise.core.sourceControl.setProvider", args)
        return tuple([LogItem.from_dict(result["log"])] if result is not None else [])
