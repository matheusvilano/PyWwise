# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from importlib import import_module as _import_module


class LazyModule:
    """A proxy for lazy-importing modules."""
    
    def __init__(self, module_name: str):
        """
        Stores a module name, which will be lazy-initialized (deferred).
        :param module_name: The name of the module.
        """
        self.module_name = module_name
        self._module = None
    
    def __getattr__(self, name):
        """
        During the first access,
        :param name:
        :return:
        """
        if self._module is None:
            self._module = _import_module(self.module_name)
        return getattr(self._module, name)
