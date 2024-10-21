# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient

from pywwise.aliases import ListOrTuple
from pywwise.decorators import callback
from pywwise.enums import ELogChannel, ELogSeverity
from pywwise.statics import EnumStatics
from pywwise.structs import LogItem


class Log:
    """ak.wwise.core.log"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
        
        self.item_added = _RefEvent(ELogChannel, LogItem)
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_log_itemadded.html
        \nSent when an item is added to the log. To retrieve the complete log, refer to `ak.wwise.core.log.get`.
        \n**Event Data**:
        \n- The channel on which the item was added.
        \n- The item added to the log.
        """
        
        self._item_added = self._client.subscribe("ak.wwise.core.log.itemAdded", self._on_item_added)
    
    @callback
    def _on_item_added(self, event: _RefEvent, **kwargs):
        """
        Callback function for the `itemAdded` event.
        :param event: The event to broadcast.
        :param kwargs: The event data.
        """
        channel = EnumStatics.from_value(ELogChannel, kwargs["channel"])
        item = LogItem(severity=EnumStatics.from_value(ELogSeverity, kwargs["item"]["severity"]),
                       time=kwargs["item"]["time"],
                       id=kwargs["item"]["messageId"],
                       description=kwargs["item"]["message"])
        event(channel, item)
    
    def add_item(self, message: str, severity: ELogSeverity = ELogSeverity.MESSAGE,
                 channel: ELogChannel = ELogChannel.GENERAL) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_log_additem.html \n
        Adds a new item to the logs on the specified channel.
        :param message: The text of the message to add.
        :param severity: The severity of the message to add.
        :param channel: The channel on which to add the message.
        :return: Whether the call succeeded.
        """
        args = {"message": message, "severity": severity.value, "channel": channel.value}
        return self._client.call("ak.wwise.core.log.addItem", args) is not None
    
    def clear(self, channels: ELogChannel | ListOrTuple[ELogChannel] = None) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_log_clear.html \n
        Clears the logs on one or more channels.
        :param channels: The channel or channels to clear. Duplicates will be ignored. If `None`, all channels will be
                         cleared.
        :return: Whether the call succeeded.
        """
        if channels is None:
            channels = tuple(EnumStatics.get_all_members(ELogChannel))
        elif isinstance(channels, ELogChannel):
            channels = (channels,)  # convert single value to a collection, so the loop below still works
        
        returns = list[bool]()
        for channel in channels:
            args = {"channel": channel}
            returns.append(self._client.call("ak.wwise.core.log.clear", args) is not None)
        
        return all(returns)
    
    def get(self, channel: ELogChannel = ELogChannel.GENERAL) -> tuple[LogItem, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_log_get.html \n
        Retrieves the latest log for a specific channel. Refer to `ak.wwise.core.log.item_added` to be
        notified when an item is added to the log. The log is empty when used in WwiseConsole.
        :param channel: The channel to clear.
        :return: A tuple of log items. May be empty.
        """
        args = {"channel": channel.value}
        result = self._client.call("ak.wwise.core.log.get", args)
        return tuple(LogItem(severity=EnumStatics.from_value(ELogSeverity, item["severity"]),
                             time=item["time"],
                             id=item["messageId"],
                             description=item["message"])
                     for item in result.get("items", ()))
