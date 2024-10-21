# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient

from pywwise.decorators import callback
from pywwise.enums import ECaptureLogItemType, ECaptureLogSeverity
from pywwise.primitives import GameObjectID, GUID, Name, PlayingID, ShortID
from pywwise.statics import EnumStatics
from pywwise.structs import CaptureLogItem


class CaptureLog:
    """ak.wwise.core.profiler.capture_log"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
        
        self.item_added = _RefEvent(CaptureLogItem)
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_capturelog_itemadded.html
        \nSent when a new entry is added to the capture log.
        \n**Event Data**:
        \n- An instance of CaptureLogItem, which contains information such as type, time, severity, etc.
        """
        
        self._item_added = self._client.subscribe("ak.wwise.core.profiler.captureLog.itemAdded", self._on_item_added)
    
    @callback
    def _on_item_added(self, event: _RefEvent, **kwargs):
        """
        Callback function for the `itemAdded` event.
        :param event: The event to broadcast.
        :param kwargs: The event data.
        """
        item_type = EnumStatics.from_value(ECaptureLogItemType, str(kwargs["type"]).replace(" ", ""))
        time_seconds = kwargs["time"]
        description = kwargs["description"]
        severity = EnumStatics.from_value(ECaptureLogSeverity, kwargs["severity"])
        wwise_obj_id = GUID(kwargs["objectId"]) if "objectId" in kwargs else GUID.get_null()
        wwise_obj_name = Name(kwargs["objectName"]) if "objectName" in kwargs else Name.get_null()
        wwise_obj_short = ShortID(kwargs["objectShortId"]) if "objectShortId" in kwargs else ShortID.get_null()
        game_obj_id = GameObjectID(kwargs["gameObjectId"]) if "gameObjectId" in kwargs else GameObjectID.get_null()
        game_obj_name = Name(kwargs["gameObjectName"]) if "gameObjectName" in kwargs else Name.get_null()
        playing_id = PlayingID(kwargs["playingId"]) if "playingId" in kwargs else PlayingID.get_null()
        error_code_name = kwargs.get("errorCodeName", "")
        event(CaptureLogItem(item_type, time_seconds, description, severity, wwise_obj_id, wwise_obj_name,
                             wwise_obj_short, game_obj_id, game_obj_name, playing_id, error_code_name))
