# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from typing import Callable as _Callable


def callback(func: _Callable) -> _Callable:
    """
    A decorator for PyWwise callbacks. Checks if the associated event is valid and has any subscribers. If it has at
    least one subscriber, it will be broadcast. For the decorated function to work properly: \n
    - its name should start with the prefix `_on_` (e.g. `_on_event_happened`).
    - its associated event should have the same name, minus the prefix `_on_` (e.g. `event_happened`).
    - both the decorated function and the associated event should be encapsulated within the same object.
    :param func: The function to decorate.
    :return: The decorated function.
    """
    
    def wrapper(self, **kwargs):
        event = getattr(self, func.__name__[4:])  # removing the prefix "_on_" gives the RefEvent
        if event is None:
            raise NameError(f"Function '{func.__name__}' missing associated event: '{func.__name__[4:]}'.")
        if len(event) > 0:
            return func(self, event, **kwargs)
    
    return wrapper


def console_instance_only(func: _Callable) -> _Callable:
    """
    A decorator for functions that can only be called on a console instance of Wwise. Checks the owner object's
    `is_console_instance` (or, alternatively, `_is_console_instance`); if `None` or `False`, the decorated function will
    NOT be called and an exception is raised. Note: if there is no owner object, the check defaults to `None`. \n
    :param func: The function to decorate.
    :raise: NameError - if `is_console_instance` does not exist.
    :raise: ValueError - if `is_console_instance` is False.
    :return: The decorated function.
    """
    attr_name = "is_console_instance"
    
    def wrapper(self, *args, **kwargs):
        flag = getattr(self, attr_name) \
            if hasattr(self, attr_name) \
            else getattr(self, f"_{attr_name}", None)
        if flag is None:
            raise NameError(f"Object '{self}' does not have an attribute named '{attr_name}'.")
        if flag is True:
            raise ValueError(f"Debug function called on a non-console instance of 'Ak'.")
        return func(self, *args, **kwargs)
    
    return wrapper


def debug_build_only(func: _Callable) -> _Callable:
    """
    A decorator for PyWwise debug-only functions. Checks the owner object's `is_debug_build` (or, alternatively,
    `_is_debug_build`); if `None` or `False`, the decorated function will NOT be called and an exception is raised.
    Note: if there is no owner object, the check defaults to `None`. \n
    :param func: The function to decorate.
    :raise: NameError - if `is_debug_build` does not exist.
    :raise: ValueError - if `is_debug_build` is False.
    :return: The decorated function.
    """
    attr_name = "is_debug_build"
    
    def wrapper(self, *args, **kwargs):
        flag = getattr(self, attr_name) \
            if hasattr(self, attr_name) \
            else getattr(self, f"_{attr_name}", None)
        if flag is None:
            raise NameError(f"Object '{self}' does not have an attribute named '{attr_name}'.")
        if flag is True:
            raise ValueError(f"Debug function called on a non-debug instance of 'Ak'.")
        return func(self, *args, **kwargs)
    
    return wrapper
