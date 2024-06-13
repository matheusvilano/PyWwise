from typing import Any as _Any
from waapi import SequentialThreadExecutor as _SequentialThreadExecutor
from pywwise.ak import Ak as _Ak


def new(url: _Any = None, allow_exception: bool = False,
        callback_executor: _Any = _SequentialThreadExecutor) -> _Ak:
	"""
	:param url: URL of the Wwise Authoring API WAMP server, defaults to ws://127.0.0.1:8080/waapi
	:param allow_exception: Allow errors on call and subscribe to throw an exception. Default is False.
	:param callback_executor: Executor strategy for event callbacks
	"""
	return _Ak(url, allow_exception, callback_executor)
