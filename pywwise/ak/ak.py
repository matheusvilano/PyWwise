from typing import Any
from waapi import WaapiClient as _WaapiClient, SequentialThreadExecutor as _SequentialThreadExecutor
from pywwise.ak.soundengine import SoundEngine as _SoundEngine
from pywwise.ak.wwise import Wwise as _Wwise


class Ak:
    """ak"""

    def __init__(self, url: Any = None, allow_exception: bool = False,
                 callback_executor: Any = _SequentialThreadExecutor):
        """
        :param url: URL of the Wwise Authoring API WAMP server, defaults to ws://127.0.0.1:8080/waapi
        :param allow_exception: Allow errors on call and subscribe to throw an exception. Default is False.
        :param callback_executor: Executor strategy for event callbacks
        """
        self._client = _WaapiClient(url, allow_exception, callback_executor)
        self.soundengine = _SoundEngine(self._client)
        self.wwise = _Wwise(self._client)
