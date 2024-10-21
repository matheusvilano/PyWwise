# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient

from pywwise.structs import WwiseObjectWatch
from pywwise.waapi.ak.wwise.console import Console as _Console
from pywwise.waapi.ak.wwise.core import Core as _Core
from pywwise.waapi.ak.wwise.debug import Debug as _Debug
from pywwise.waapi.ak.wwise.ui import UI as _UI
from pywwise.waapi.ak.wwise.waapi import Waapi as _Waapi


class Wwise:
    """ak.wwise"""
    
    def __init__(self, client: _WaapiClient, is_debug_build: bool = False, is_console_instance: bool = False,
                 watch_list: tuple[WwiseObjectWatch, ...] = ()):
        """
        Constructor.
        :param client: The WAAPI client to use.
        :param is_debug_build: Should be set to true if the instance of Wwise is a debug build and debug-only
                               functions/topics are required.
        :param is_console_instance: Should be set to true if the instance of Wwise is running in a console window.
        :param watch_list: A tuple of `WwiseObjectWatch` instances. This will be used to set up the
                           `ak.wwise.core.object.property_changed` event.
        """
        self._client = client
        self.console = _Console(client, is_console_instance)
        self.core = _Core(client, watch_list)
        self.debug = _Debug(client, is_debug_build)
        self.ui = _UI(client)
        self.waapi = _Waapi(client)
