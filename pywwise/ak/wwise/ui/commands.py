from waapi import WaapiClient as _WaapiClient
from pywwise.structs import WwiseObjectInfo as _WwiseObjectInfo
from pywwise.structs import PlatformInfo as _PlatformInfo, CommandInfo as _CommandInfo


class Commands:
    """ak.wwise.ui.commands"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def get_commands(self):
        """
        Gets the list of commands.
        """

    def execute(self, command: str, objects: set[_WwiseObjectInfo] = None, platforms: set[_PlatformInfo] = None,
                value: str | float | bool = None) -> None:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_commands_execute.html \n
        Executes a command. Some commands can take a list of objects as parameters. Refer to Wwise
        Authoring Command Identifiers for the available commands.
        :param command: The ID of the command to execute. Refer to Wwise Authoring Command Identifiers for the lists of
        commands.
        :param objects: An array of objects. Each object is an ID (GUID), name, or path of the object. Some commands can
        take objects as arguments. Refer to the commands for more information.
        :param platforms: An array of platform. Each platform is an ID (GUID) or a unique name. Some commands can take
        platforms as arguments. Refer to the commands for more information.
        :param value: A value to pass to the command. Some commands can take a value as an argument. **Can be Null,
        String, Float, or Bool**. Refer to the commands for more information.
        """
        if command is None:
            return

        args = {"command": command, "objects": list(), "platforms": list(), "value": None}

        if objects is not None:
            for object in objects:
                return
        if platforms is not None:
            for platform in platforms:
                if platform.guid:
                    args["platforms"].append(platform.guid)
                elif platform.name:
                    args["platforms"].append(platform.name)
        if value is not None:
            args["value"] = value

        return self._client.call("ak.wwise.ui.commands.execute", args)

    def register(self, commands: set[_CommandInfo] = None) -> None:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_commands_register.html \n
        Registers an array of add-on commands. Registered commands remain until the Wwise process is
        terminated. Refer to Defining Command Add-ons for more information about registering commands.
        Also refer to `ak.wwise.ui.commands.executed`.
        :param commands: An array of add-on commands. Data for the commands to be registered.
        """
        if commands is None:
            return

        args = {"commands": list()}

        for command in commands:
            args["commands"].append(command)

        return self._client.call("ak.wwise.ui.commands.register", args)

    def unregister(self, commands: set[_CommandInfo] = None) -> None:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_commands_unregister.html \n
        Unregisters an array of add-on UI commands.
        """
        if commands is None:
            return

        args = {"commands": list()}

        for command in commands:
            args["commands"].append(command.id)

        return self._client.call("ak.wwise.ui.commands.unregister", args)