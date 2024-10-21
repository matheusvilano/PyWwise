# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient

from pywwise.waapi.ak.wwise.console.project import Project as _Project


class Console:
    """ak.wwise.console"""
    
    def __init__(self, client: _WaapiClient, is_console_instance: bool = False):
        """
        Constructor.
        :param client: The WAAPI client to use.
        :param is_console_instance: Should be set to true if the instance of Wwise is running in a console window.
        """
        self._client = client
        self.project = _Project(self._client, is_console_instance)
