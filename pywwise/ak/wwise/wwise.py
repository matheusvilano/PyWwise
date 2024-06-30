from waapi import WaapiClient as _WaapiClient
from pywwise.ak.wwise.console import Console as _Console
from pywwise.ak.wwise.debug import Debug as _Debug
from pywwise.ak.wwise.core import Core as _Core
from pywwise.ak.wwise.ui import UI as _UI
from pywwise.ak.wwise.waapi import Waapi as _Waapi


class Wwise:
	"""ak.wwise"""
	
	def __init__(self, client: _WaapiClient, is_debug_build: bool = False):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		:param is_debug_build: Should be set to true if the instance of Wwise is a debug build and debug-only
		functions/topics are required.
		"""
		self._client = client
		self.console = _Console(client)
		self.core = _Core(client)
		self.debug = _Debug(client, is_debug_build)
		self.ui = _UI(client)
		self.waapi = _Waapi(client)
