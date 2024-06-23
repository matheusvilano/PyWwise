import unittest
import pywwise
from pywwise.enums import *
from pywwise.types import *
from pywwise.structs import *
from constants import *

ak = pywwise.new()

class AkWwiseUiUiTest(unittest.TestCase):
	
	def test__bring_to_foreground(self):
		results = ak.wwise.ui.bring_to_foreground()
		self.assertIsNotNone(results)
	
	def test__capture_screen(self):
		captureRect = CaptureRect(0, 0, 1080, 1920)
		results = ak.wwise.ui.capture_screen("Batch Rename", 1, captureRect)
		self.assertIsInstance(results, tuple)
		self.assertEqual(len(results), 2)
		self.assertIsInstance(results[0], str)
		self.assertIsInstance(results[1], str)

	def test__get_selected_objects(self):
		returnOptions = EReturnOptions.WORK_UNIT
		results = ak.wwise.ui.get_selected_objects(returnOptions, "Windows", "English(US)")
		self.assertIsInstance(results, list)
		for result in results:
			print(result)

if __name__ == '__main__':
	unittest.main()
