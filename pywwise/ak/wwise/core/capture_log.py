from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient
from pywwise.decorators import callback
from pywwise.enums import ECaptureLogItemType, ECaptureLogSeverity
from pywwise.statics import EnumStatics
from pywwise.structs import CaptureLogItem
from pywwise.types import GameObjectID, GUID, Name, PlayingID, ShortID


class CaptureLog:
	"""ak.wwise.core.profiler.capture_log"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
		
		# TODO: implement topics
		self.item_added = _RefEvent(CaptureLogItem)
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_capturelog_itemadded.html
		\nSent when a new entry is added to the capture log.
		\n**Event Data**:
		\n- An instance of CaptureLogItem, which contains information such as type, time, severity, etc.
		"""
		
		self._item_added = self._client.subscribe("ak.wwise.core.profiler.captureLog.itemAdded", self._on_item_added)
	
	@callback
	def _on_item_added(self, **kwargs):
		"""
		Callback function for the `item_added` event.
		:param kwargs: The event data.
		"""
		#
		item_type = EnumStatics.from_value(ECaptureLogItemType, str(kwargs["type"]).replace(" ", ""))
		time_seconds = kwargs["time"]
		description = kwargs["description"]
		severity = EnumStatics.from_value(ECaptureLogSeverity, kwargs["severity"])
		wwise_obj_id = GUID(kwargs["objectId"]) if "objectId" in kwargs else GUID.get_zero()
		wwise_obj_name = Name(kwargs["objectName"]) if "objectName" in kwargs else Name.get_null()
		wwise_obj_short = ShortID(kwargs["objectShortId"]) if "objectShortId" in kwargs else ShortID.get_invalid()
		game_obj_id = GameObjectID(kwargs["gameObjectId"]) if "gameObjectId" in kwargs else GameObjectID.get_invalid()
		game_obj_name = Name(kwargs["gameObjectName"]) if "gameObjectName" in kwargs else Name.get_null()
		playing_id = PlayingID(kwargs["playingId"]) if "playingId" in kwargs else PlayingID.get_invalid()
		error_code_name = kwargs.get("errorCodeName", "")
		self.item_added(CaptureLogItem(item_type, time_seconds, description, severity, wwise_obj_id, wwise_obj_name,
		                               wwise_obj_short, game_obj_id, game_obj_name, playing_id, error_code_name))
