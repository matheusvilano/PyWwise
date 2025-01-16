# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient

from pywwise.aliases import SystemPath
from pywwise.structs import ConnectionStatusInfo, RemoteConsoleInformation


class Remote:
    """ak.wwise.core.remote"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
    
    def connect(self, host: str | SystemPath, app_name: str = None, command_port: int = None) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_remote_connect.html \n
        Connects the Wwise Authoring application to a Wwise Sound Engine running executable or to a saved
        profile file. The host must be running code with communication enabled. If only "host" is
        provided, Wwise connects to the first Sound Engine instance found. To distinguish between
        different instances, you can also provide the name of the application to connect to.
        :param host: The host to connect to.The host can be a computer name, an IPv4 address, an IP:PORT pair, or a
                     full path to a saved capture (.prof file). Use 127.0.0.1 to connect to localhost.
        :param app_name: The value in the Application Name column from the Remote Connection dialog in Wwise, or from
                         the get_available_consoles() method. If you are running more than one Sound Engine instance,
                         you can specify the name of the application to connect to.
        :param command_port: The command port. If you are running two or more Sound Engine instances that use the same
                             application name, you can specify the command port to distinguish between different
                             applications sharing the same name. You don't need to use this if the application name
                             is unique. When using this, you must also provide appName. You can obtain this information
                             from the get_available_consoles() method.
        :return: True if the connection is successful, False otherwise.
        """
        args = {"host": host}
        
        if app_name is not None:
            args["appName"] = app_name
        
        if command_port is not None and app_name is None:
            return False
        else:
            args["appName"] = app_name
            args["commandPort"] = command_port
        
        return self._client.call("ak.wwise.core.remote.connect", args) is not None
    
    def disconnect(self) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_remote_disconnect.html \n
        Disconnects the Wwise Authoring application from a connected Wwise Sound Engine running executable.
        :return: True if the disconnection is successful, False otherwise.
        """
        return self._client.call("ak.wwise.core.remote.disconnect", {}) is not None
    
    def get_available_consoles(self) -> tuple[RemoteConsoleInformation, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_remote_getavailableconsoles.html \n
        Retrieves all consoles available for connecting Wwise Authoring to a Sound Engine instance.
        :return: A tuple of RemoteConsoleInformation objects. Each object represents an available remote console.
        """
        results = self._client.call("ak.wwise.core.remote.getAvailableConsoles", {})
        
        if results is None:
            return tuple()
        
        results = results.get("consoles")
        
        if results is None:
            return tuple()
        
        consoles = [RemoteConsoleInformation(
            name=console.get("name", ""),
            platform=console.get("platform", ""),
            custom_platform=console.get("customPlatform", ""),
            host=console.get("host", ""),
            app_name=console.get("appName", ""),
            command_port=console.get("commandPort", -1),
        ) for console in results]
        
        return tuple(consoles)
    
    def get_connection_status(self) -> ConnectionStatusInfo:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_remote_getconnectionstatus.html \n
        Retrieves the connection status.
        :return: A ConnectionStatusInfo object, detailing into more detail the state of current connection.
        """
        result = self._client.call("ak.wwise.core.remote.getConnectionStatus", {})
        
        if result is None:
            result = dict()
        
        console = result.get("console", dict())
        console = RemoteConsoleInformation(
            name=console.get("name", ""),
            platform=console.get("platform", ""),
            custom_platform=console.get("customPlatform", ""),
            host=console.get("host", ""),
            app_name=console.get("appName", ""),
            command_port=console.get("commandPort", -1))
        
        return ConnectionStatusInfo(is_connected=result.get("isConnected", False),
                                    status=result.get("status", "Failed to retrieve connection status."),
                                    console=console)
