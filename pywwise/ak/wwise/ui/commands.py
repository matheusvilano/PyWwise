from waapi import WaapiClient as _WaapiClient
from pywwise.structs import WwiseObjectInfo as _WwiseObjectInfo
from pywwise.structs import PlatformInfo as _PlatformInfo, CommandInfo as _CommandInfo
from pywwise.types import GUID as _GUID, ShortID as _ShortID, ProjectPath as _ProjectPath, Name as _Name
from pywwise.enums import ECommand as _ECommand


class Commands:
    """ak.wwise.ui.commands"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def get_commands(self) -> list[str]:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_commands_getcommands.html \n
        Gets the list of commands.
        :return: The set of available commands.
        """
        results = self._client.call("ak.wwise.ui.commands.getCommands")
        return results.get("commands")

    def execute(self, command: _ECommand, objects: set[_WwiseObjectInfo | _GUID | _ProjectPath | _Name | _ShortID] = None,
                platforms: set[_PlatformInfo | _Name | _GUID] = None, value: str | float | bool = None) -> None:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_commands_execute.html \n
        Executes a command. Some commands can take a list of objects as parameters. Refer to Wwise
        Authoring Command Identifiers for the available commands.
        :param command: The ID of the command to execute. Refer to Wwise Authoring Command Identifiers for the lists of
        commands.
        :param objects: For commands that take objects as arguments. This set should contain the GUID, project path,
        name, and/or short ID of the Wwise objects being passed to the command to be executed. NOTE: although Name and
        ShortID are both supported, they are NOT recommended. For a Name, you will need to follow the format "Type:Name"
        (e.g. Name("Event:PlayMySound")); for ShortID, only "global" types (e.g. State Groups) will work.
        :param platforms: An array of platform. Each platform is a GUID or a Name. Some commands can take
        platforms as arguments. Refer to the commands for more information.
        :param value: A value to pass to the command. Some commands can take a value as an argument. **Can be Null,
        String, Float, or Bool**. Refer to the commands for more information.
        """
        if command is None:
            return

        args = {"command": command, "objects": list(), "platforms": list(), "value": None}

        if objects is not None:
            for wwise_object in objects:
                match wwise_object:
                    case _WwiseObjectInfo():
                        args["objects"].append(wwise_object.guid)
                    case _GUID() | _ProjectPath() | _Name():
                        args["objects"].append(wwise_object)
                    case _ShortID():
                        args["objects"].append(f"Global:{wwise_object}")
                    case _:
                        args["objects"].append(str(wwise_object))
        if platforms is not None:
            for platform in platforms:
                match platform:
                    case _GUID() | _Name():
                        args["platforms"].append(platform)
                    case _PlatformInfo():
                        args["platforms"].append(platform.guid)
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
            args["commands"].append(command.dictionary)

        return self._client.call("ak.wwise.ui.commands.register", args)

    def unregister(self, commands: set[_CommandInfo | str] = None) -> None:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_commands_unregister.html \n
        Unregisters an array of add-on UI commands.
        """
        if commands is None:
            return

        args = {"commands": list()}

        for command in commands:
            if isinstance(command, _CommandInfo):
                args["commands"].append(command.id)
            else:
                args["commands"].append(str(command))

        return self._client.call("ak.wwise.ui.commands.unregister", args)
