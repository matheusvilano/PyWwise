# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from asyncio import new_event_loop as asyncio_new_event_loop, set_event_loop as asyncio_set_event_loop
from unittest import TestCase

from pywwise import new_waapi_connection


class PyWwiseTest(TestCase):
    """Base class for PyWwise test cases. Handles instantiating and deleting Ak instances automatically."""
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        asyncio_set_event_loop(asyncio_new_event_loop())
        cls.ak = new_waapi_connection()
    
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        del cls.ak
