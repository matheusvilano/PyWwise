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
		capture_rect = Rect(0, 0, 1080, 1920)
		output_path = SystemPath(r"C:\Users\juanf\OneDrive\Pictures\Test.png")
		results = ak.wwise.ui.capture_screen("Batch Rename", 1, capture_rect, output_path)
		self.assertIsInstance(results, tuple)
		self.assertEqual(len(results), 2)
		self.assertIsInstance(results[0], str)
		self.assertIsInstance(results[1], str)
		self.assertTrue(output_path.exists())

	def test__get_selected_objects(self):
		objects = ak.wwise.ui.get_selected_objects(platform="Windows", language="English(US)")
		if objects is not None:
			self.assertGreaterEqual(len(objects), 1)
			self.assertEqual(len(objects[0]), 3)  # guid, name, {}
		objects = ak.wwise.ui.get_selected_objects({EReturnOptions.WORK_UNIT, EReturnOptions.TYPE}, "Windows", "English(US)")
		if objects is not None:
			self.assertGreaterEqual(len(objects), 1)
			self.assertEqual(len(objects[0]), 3)  # guid, name, {work_unit, type}
			self.assertEqual(len(objects[0][2]), 2)


if __name__ == '__main__':
	unittest.main()
