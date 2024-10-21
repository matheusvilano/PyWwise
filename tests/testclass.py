# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

import asyncio
from unittest import TestCase

from pywwise import new_waapi_connection as ak_new


class PyWwiseTest(TestCase):
    """Base class for PyWwise test cases. Handles instantiating and deleting Ak instances automatically."""
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        asyncio.set_event_loop(asyncio.new_event_loop())
        cls.ak = ak_new()
    
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        del cls.ak
