import time
import unittest
import pywwise
from pywwise.enums import *
from pywwise.types import *
from pywwise.structs import *
from constants import *

ak = pywwise.new()


class AkWwiseDebugTest(unittest.TestCase):
	def test__item_added(self):
		def on_item_added(channel: ELogChannel, item: LogItem):
			self.assertIsNotNone(channel)
			self.assertIsNotNone(item)
			print(f"{channel} | {item}")
		ak.wwise.core.log.item_added += on_item_added
		time.sleep(10)  # can be replaced with ak.wwise.soundbank.generate later


if __name__ == '__main__':
	unittest.main()
