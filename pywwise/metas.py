# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

class SingletonMeta(type):
    """Metaclass for singletons."""
    
    _instances = dict()
    """A dictionary where the keys are classes and the values are instances."""
    
    def __call__(cls, *args, **kwargs):
        """
        Operator `()`.
        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        :return: The singleton instance of the `cls` class.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class StaticMeta(type):
    """Metaclass for statics."""
    
    def __call__(cls, *args, **kwargs):
        """
        Operator `()`. Will prevent the creation of a new instance.
        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        :raise: TypeError, as a static class must not have any instances of itself.
        """
        raise TypeError(f"Cannot instantiate a static class. Use '{cls.__name__}.function_name()' instead.")
