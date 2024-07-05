from waapi import (CallbackExecutor as _CallbackExecutor, SequentialThreadExecutor as _SequentialThreadExecutor,
                   WaapiClient as _WaapiClient)
from pywwise.ak.soundengine import SoundEngine as _SoundEngine
from pywwise.ak.wwise import Wwise as _Wwise


class Ak:
	"""ak"""
	
	def __init__(self, url: str = "ws://127.0.0.1:8080/waapi", allow_exception: bool = False,
	             callback_executor: _CallbackExecutor = _SequentialThreadExecutor,
	             is_debug_build: bool = False, is_console_instance: bool = False):
		"""
		:param url: URL of the Wwise Authoring API WAMP server, defaults to `ws://127.0.0.1:8080/waapi`.
		:param allow_exception: Allow errors on call and subscribe to throw an exception. Default is False.
		:param callback_executor: Executor strategy for event callbacks.
		:param is_debug_build: Should be set to true if the instance of Wwise is a debug build and debug-only.
		:param is_console_instance: Should be set to true if the instance of Wwise is running in a console window.
		functions/topics are required.
		"""
		self._client = _WaapiClient(url, allow_exception, callback_executor)
		self.soundengine = _SoundEngine(self._client)
		self.wwise = _Wwise(self._client, is_debug_build, is_console_instance)
	
	def __del__(self):
		"""Disconnect from Wwise."""
		self._client.disconnect()
