# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient

from pywwise.decorators import callback
from pywwise.enums import ECommand, EObjectType, EReturnOptions
from pywwise.primitives import GUID, Name, ProjectPath, ShortID
from pywwise.statics import EnumStatics
from pywwise.structs import CommandInfo, PlatformInfo, WwiseObjectInfo


class Commands:
    """ak.wwise.ui.commands"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
        
        self.executed = _RefEvent(ECommand, tuple[WwiseObjectInfo, ...], tuple[str, ...])
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_ui_commands_executed.html
        \nSent when a command is executed. The objects for which the command is executed are sent in the publication.
        \n**Event Data**:
        \n- The command that was executed.
        \n- A tuple of objects (WwiseObjectInfo instances) for which the command was executed. May be empty.
        \n- A tuple of platforms (GUID or name, as a string) for which the command was executed.
        """
        
        executed_options = {"return": [EReturnOptions.GUID.value, EReturnOptions.NAME.value,
                                       EReturnOptions.TYPE.value, EReturnOptions.PATH.value]}
        self._executed = self._client.subscribe("ak.wwise.ui.commands.executed", self._on_executed,
                                                executed_options)
    
    @callback
    def _on_executed(self, event: _RefEvent, **kwargs):
        """
        Callback function for the `executed` event.
        :param event: The event to broadcast.
        :param kwargs: The event data.
        """
        command = EnumStatics.from_value(ECommand, kwargs["command"])
        objs = tuple([WwiseObjectInfo.from_dict(obj) for obj in kwargs["objects"]])
        platforms = tuple(kwargs["platforms"])
        event(command, objs, platforms)
    
    def get_commands(self) -> tuple[str, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_ui_commands_getcommands.html \n
        Gets the list of commands.
        :return: A tuple containing the available commands. If empty, the call failed.
        """
        commands = self._client.call("ak.wwise.ui.commands.getCommands").get("commands")
        return tuple(commands) if commands is not None else ()
    
    def execute(self, command: ECommand,
                objects: tuple[WwiseObjectInfo | GUID | ProjectPath | ShortID | tuple[EObjectType, Name]] = None,
                platforms: set[PlatformInfo | Name | GUID] = None, value: str | float | bool = None) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_ui_commands_execute.html \n
        Executes a command. Some commands can take a list of objects as parameters. Refer to Wwise
        Authoring Command Identifiers for the available commands.
        :param command: The ID of the command to execute. Refer to Wwise Authoring Command Identifiers for the lists of
                        commands.
        :param objects: For commands that take objects as arguments. This set should contain the GUID or project path
                        of the Wwise objects being passed to the command to be executed. Name and ShortID are both
                        supported, but are NOT recommended, as they will only work with "global" types (e.g. State
                        Groups, Events, etc.). To use a Name, you will need to pass a tuple containing the object type
                        and the actual name; for ShortID, only "global" types (e.g. State Groups) will work.
        :param platforms: An array of platform. Each platform is a GUID or a Name. Some commands can take
                          platforms as arguments. Refer to the commands for more information.
        :param value: A value to pass to the command. Some commands can take a value as an argument. **Can be Null,
                      String, Float, or Bool**. Refer to the commands for more information.
        :return: Whether the call succeeded.
        """
        if command is None:
            return False
        
        args = {"command": command, "objects": list(), "platforms": list(), "value": None}
        
        if objects is not None:
            for wwise_object in objects:
                match wwise_object:
                    case WwiseObjectInfo():
                        args["objects"].append(wwise_object.guid)
                    case GUID() | ProjectPath() | Name():
                        args["objects"].append(wwise_object)
                    case ShortID():  # "Global:0123456789"
                        args["objects"].append(f"Global:{wwise_object}")
                    case tuple():  # "Type:Name"
                        args["objects"].append(f"{wwise_object[0].value}:{wwise_object[1]}")
                    case _:
                        args["objects"].append(str(wwise_object))
        if platforms is not None:
            for platform in platforms:
                match platform:
                    case GUID() | Name():
                        args["platforms"].append(platform)
                    case PlatformInfo():
                        args["platforms"].append(platform.guid)
        if value is not None:
            args["value"] = value
        
        return self._client.call("ak.wwise.ui.commands.execute", args) is not None
    
    def register(self, commands: set[CommandInfo]) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_ui_commands_register.html \n
        Registers an array of add-on commands. Registered commands remain until the Wwise process is
        terminated. Refer to Defining Command Add-ons for more information about registering commands.
        Also refer to `ak.wwise.ui.commands.executed`.
        :param commands: An array of add-on commands. Data for the commands to be registered.
        :return: Whether the call succeeded.
        """
        if commands is None:
            return False
        
        args = {"commands": list()}
        
        for command in commands:
            args["commands"].append(command.dictionary)
        
        return self._client.call("ak.wwise.ui.commands.register", args) is not None
    
    def unregister(self, commands: set[CommandInfo | str]) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_ui_commands_unregister.html \n
        Unregisters an array of add-on UI commands.
        :param commands: A set of add-on commands. Can either be a string containing the add-on command ID or a full
                         Add-on Command Info instance.
        :return: Whether the call succeeded.
        """
        if commands is None:
            return False
        
        args = {"commands": list()}
        
        for command in commands:
            if isinstance(command, CommandInfo):
                args["commands"].append(command.id)
            else:
                args["commands"].append(str(command))
        
        return self._client.call("ak.wwise.ui.commands.unregister", args) is not None
