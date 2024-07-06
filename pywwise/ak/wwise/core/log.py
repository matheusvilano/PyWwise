from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient

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
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_log_itemadded.html
        \nSent when an item is added to the log. To retrieve the complete log, refer to `ak.wwise.core.log.get`.
        \n**Event Data**:
        \n- The channel on which the item was added.
        \n- The item added to the log.
        """
		
		self._item_added = self._client.subscribe("ak.wwise.core.log.itemAdded", self._on_item_added)
	
	@callback
	def _on_item_added(self, **kwargs):
		"""
		Callback function for the `itemAdded` event.
		:param kwargs: The event data.
		"""
		channel = EnumStatics.from_value(ELogChannel, kwargs["channel"])
		item = LogItem(severity=EnumStatics.from_value(ELogSeverity, kwargs["item"]["severity"]),
		               time=kwargs["item"]["time"],
		               id=kwargs["item"]["messageId"],
		               description=kwargs["item"]["message"])
		self.item_added(channel, item)
	
	def add_item(self):
		"""
		Adds a new item to the logs on the specified channel.
		"""
	
	def clear(self):
		"""
		Clears the logs on the specified channel.
		"""
	
	def get(self):
		"""
		Retrieves the latest log for a specific channel. Refer to `ak.wwise.core.log.item_added` to be
		notified when an item is added to the log. The log is empty when used in WwiseConsole.
		"""
