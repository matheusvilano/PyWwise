import unittest

import pywwise
from pywwise.enums import *
from pywwise.structs import *

ak = pywwise.new_waapi_connection()


class AkWwiseDebugTest(unittest.TestCase):
	
	def test__add(self):
		self.assertTrue(ak.wwise.core.log.add_item("UnitTest"))
	
	def test__clear(self):
		self.assertTrue(ak.wwise.core.log.clear())
	
	def test__get(self):
		items = ak.wwise.core.log.get(ELogChannel.GENERAL)
		self.assertIsNotNone(items)
		print(items)
	
	def test__item_added(self):
		def on_item_added(channel: ELogChannel, item: LogItem):
			self.assertIsNotNone(channel)
			self.assertIsNotNone(item)
			print(f"{channel} | {item}")
		
		ak.wwise.core.log.item_added += on_item_added
		ak.wwise.core.log.add_item("UnitTest")


if __name__ == '__main__':
	unittest.main()
