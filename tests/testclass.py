import asyncio
from unittest import TestCase

from pywwise import new as ak_new
from pywwise.ak import Ak


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
