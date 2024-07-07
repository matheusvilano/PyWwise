from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient


class CaptureLog:
	"""ak.wwise.core.profiler.capture_log"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
		
		# TODO: implement topics
		self.item_added: _RefEvent
	