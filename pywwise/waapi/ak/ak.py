# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from typing import Self as _Self, TypeAlias as _TypeAlias

from waapi import CallbackExecutor, SequentialThreadExecutor, WaapiClient as _WaapiClient

from pywwise.aliases import ListOrTuple
from pywwise.structs import WwiseObjectWatch
from pywwise.waapi.ak.soundengine import SoundEngine as _SoundEngine
from pywwise.waapi.ak.wwise import Wwise as _Wwise


class Ak:
    """ak"""
    
    _connections = list[_Self]()
    """List of all active connections to Wwise."""
    
    def __init__(self, url: str = "ws://127.0.0.1:8080/waapi", allow_exception: bool = False,
                 callback_executor: CallbackExecutor = SequentialThreadExecutor,
                 is_debug_build: bool = False, is_console_instance: bool = False,
                 watch_list: ListOrTuple[WwiseObjectWatch] = ()):
        """
        Constructor.
        :param url: URL of the Wwise Authoring API WAMP server, defaults to `ws://127.0.0.1:8080/waapi`.
        :param allow_exception: Allow errors on call and subscribe to throw an exception. Default is False.
        :param callback_executor: Executor strategy for event callbacks.
        :param is_debug_build: Should be set to true if the instance of Wwise is a debug build and debug-only.
        :param is_console_instance: Should be set to true if the instance of Wwise is running in a console window.
                                    functions/topics are required.
        :param watch_list: A tuple of `WwiseObjectWatch` instances. This will be used to set up the
                           `ak.wwise.core.object.property_changed` event.
        """
        self._client = _WaapiClient(url, allow_exception, callback_executor)
        self.soundengine = _SoundEngine(self._client)
        self.wwise = _Wwise(self._client, is_debug_build, is_console_instance, watch_list)
        self._connections.append(self)
    
    def __del__(self):
        """Disconnect, then delete this connection object."""
        if self.is_connected():
            self.disconnect()
    
    def __enter__(self) -> _Self:
        """
        Enter the context (re: `with` statement).
        :return: This instance of the `Ak` class.
        """
        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        """
        Exit the context (re: `with` statement).
        :param exc_type: The exception type, if any.
        :param exc_value: The exception value, if any.
        :param traceback: The traceback, if any exception(s) were raised.
        :return: Whether an exception was raised.
        """
        if self.is_connected():
            self._client.disconnect()
        return bool(exc_type)
    
    @classmethod
    def get_connections(cls) -> tuple[_Self, ...]:
        """
        Get all active connections to Wwise. Intended only for internal use or debugging. Avoid using this function
        in your logic. If you need to check if this connection is ative, use **is_connected** instead, or **disconnect**
        if you are trying to delete this connection.
        :return: The currently active connections to Wwise, in a `tuple`. This container will NOT be updated as
                 connections are created/destroyed. Also, keep in mind that connections cannot be modified this way.
        """
        return tuple(cls._connections)
    
    def is_connected(self) -> bool:
        """
        Check if this instance is connected to Wwise.
        :return: Whether this instance is connected to Wwise.
        """
        return self._client.is_connected()
    
    def disconnect(self) -> bool:
        """
        Disconnect from Wwise.
        :return: Whether the disconnection was successful.
        """
        if self in self._connections:
            self._connections.remove(self)
        return self._client.disconnect()


WwiseConnection: _TypeAlias = Ak  # This cannot exist in aliases.py due to a circular import issue.
"""Represents a connection to Wwise."""
