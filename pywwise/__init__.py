# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from logging import CRITICAL as _LEVEL_CRITICAL, getLogger as _getLogger

from waapi import CallbackExecutor, SequentialThreadExecutor

from pywwise.aliases import *
from pywwise.enums import *
from pywwise.objects import *
from pywwise.primitives import *
from pywwise.structs import *
from pywwise.waapi.ak import Ak as _Ak, WwiseConnection
from pywwise.waql import *

_getLogger("waapi").setLevel(_LEVEL_CRITICAL)


def new_waapi_connection(url: str = "ws://127.0.0.1:8080/waapi", *, allow_exception: bool = False,
                         callback_executor: CallbackExecutor = SequentialThreadExecutor,
                         is_debug_build: bool = False, is_console_instance: bool = False,
                         watch_list: tuple[WwiseObjectWatch, ...] = ()) -> WwiseConnection:
    """
    Connects to an instance of Wwise.
    :param url: URL of the Wwise Authoring API WAMP server, defaults to `ws://127.0.0.1:8080/waapi`.
    :param allow_exception: Allow errors on call and subscribe to throw an exception. Default is False.
    :param callback_executor: Executor strategy for event callbacks.
    :param is_debug_build: Should be set to true if the instance of Wwise is a debug build and debug-only.
    :param is_console_instance: Should be set to true if the instance of Wwise is running in a console window.
                                functions/topics are required.
    :param watch_list: A tuple of `WwiseObjectWatch` instances. This will be used to set up the
                       `ak.wwise.core.object.property_changed` event.
    :return: A WAAPI connection.
    """
    return _Ak(url, allow_exception, callback_executor, is_debug_build, is_console_instance, watch_list)


def set_waapi_logging(level: int):
    """
    Sets the WAAPI logger's level. By default, the logger will only log `CRITICAL` errors, which are rare. Use this
    function if you are experiencing issues with any functions/topics and would like more information from the logger.
    :param level: The level, represented as an integer. Common values: NOTSET=0, DEBUG=10, INFO=20, WARNING=30,
                  ERROR=40, CRITICAL=50.
    """
    _getLogger("waapi").setLevel(level)
