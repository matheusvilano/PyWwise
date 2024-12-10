# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient

from pywwise.aliases import SystemPath
from pywwise.decorators import callback


class Project:
    """ak.wwise.core.project"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
        
        self.loaded = _RefEvent()
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_project_loaded.html
        \nSent when the project has been successfully loaded.
        """
        
        self._loaded = self._client.subscribe("ak.wwise.core.project.loaded", self._on_loaded)
        
        self.post_closed = _RefEvent()
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_project_postclosed.html
        \nSent when the after the project is completely closed.
        """
        
        self._post_closed = self._client.subscribe("ak.wwise.core.project.postClosed", self._on_post_closed)
        
        self.pre_closed = _RefEvent()
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_project_preclosed.html
        \nSent when the project begins closing.
        """
        
        self._pre_closed = self._client.subscribe("ak.wwise.core.project.preClosed", self._on_pre_closed)
        
        self.saved = _RefEvent(tuple[SystemPath, ...])
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_project_saved.html
        \nSent when the project has been saved.
        \n**Event Data**:
        \n- A tuple containing the absolute paths to the Work Unit and Project files that were modified.
        """
        
        self._saved = self._client.subscribe("ak.wwise.core.project.saved", self._on_saved)
    
    @callback
    def _on_loaded(self, event: _RefEvent):
        """
        Callback function for the `loaded` event.
        :param event: The event to broadcast.
        """
        event()
    
    @callback
    def _on_post_closed(self, event: _RefEvent):
        """
        Callback function for the `postClosed` event.
        :param event: The event to broadcast.
        """
        event()
    
    @callback
    def _on_pre_closed(self, event: _RefEvent):
        """
        Callback function for the `preClosed` event.
        :param event: The event to broadcast.
        """
        event()
    
    @callback
    def _on_saved(self, event: _RefEvent, **kwargs):
        """
        Callback function for the `saved` event.
        :param event: The event to broadcast.
        :param kwargs: The event data.
        """
        event(tuple(SystemPath(path) for path in kwargs.get("modifiedPaths", dict())))
    
    def save(self, version_control_auto_checkout: bool = True) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_project_save.html \n
        Saves the current project.
        :param version_control_auto_checkout: Whether to automatically check out changes to version control. Only
                                              supported in Wwise 2023 or above.
        :return: Whether the operation succeeded.
        """
        args = {"autoCheckOutToSourceControl": False} if not version_control_auto_checkout else dict()
        return self._client.call("ak.wwise.core.project.save", args) is not None
