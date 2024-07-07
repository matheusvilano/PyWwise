from logging import CRITICAL as _LEVEL_CRITICAL, getLogger as _get_logger
from typing import Any as _Any
from waapi import SequentialThreadExecutor as _SequentialThreadExecutor
from pywwise.ak import Ak as _Ak

_get_logger("waapi").setLevel(_LEVEL_CRITICAL)


def new(url: _Any = None, allow_exception: bool = False,
        callback_executor: _Any = _SequentialThreadExecutor) -> _Ak:
	"""
	Connects to an instance of Wwise.
	:param url: URL of the Wwise Authoring API WAMP server, defaults to ws://127.0.0.1:8080/waapi
	:param allow_exception: Allow errors on call and subscribe to throw an exception. Default is False.
	:param callback_executor: Executor strategy for event callbacks
	"""
	return _Ak(url, allow_exception, callback_executor)


def set_logging(level: int):
	"""
	Sets the WAAPI logger's level. By default, the logger will only log `CRITICAL` errors, which are rare. Use this
	function if you are experiencing issues with any functions/topics and would like more information from the logger.
	:param level: The level, represented as an integer. Common values: NOTSET=0, DEBUG=10, INFO=20, WARNING=30,
				  ERROR=40, CRITICAL=50.
	"""
	_get_logger("waapi").setLevel(level)
