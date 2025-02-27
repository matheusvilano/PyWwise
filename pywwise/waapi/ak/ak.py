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
    
    def __enter__(self) -> _Self:
        """
        Enter the context (re: `with` statement).
        :return: This instance of the `Ak` class.
        """
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the context (re: `with` statement).
        :param exc_type: The exception type, if any.
        :param exc_value: The exception value, if any.
        :param traceback: The traceback, if any exception(s) were raised.
        :return: Whether an exception was raised.
        """
        self._client.disconnect()
        return bool(exc_type)
    
    def is_connected(self):
        """
        Check if this instance is connected to Wwise.
        :return: Whether this instance is connected to Wwise.
        """
        return self._client.is_connected()
    
    def disconnect(self):
        """Disconnect from Wwise."""
        self._client.disconnect()


WwiseConnection: _TypeAlias = Ak  # This cannot exist in aliases.py due to a circular import issue.
"""Represents a connection to Wwise."""
