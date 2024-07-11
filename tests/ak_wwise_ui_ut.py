import unittest
import pywwise
from pywwise.enums import *
from pywwise.types import *
from pywwise.structs import *
from constants import *

ak = pywwise.new_connection()


class AkWwiseUiTest(unittest.TestCase):
	
	def test__bring_to_foreground(self):
		results = ak.wwise.ui.bring_to_foreground()
		self.assertIsNotNone(results)
	
	def test__capture_screen(self):
		capture_rect = Rect(0, 0, 1080, 1920)
		output_path = RESOURCES_PROJECT__PATH / "Captures" / "Test.png"
		results = ak.wwise.ui.capture_screen("Batch Rename", 1, capture_rect, output_path)
		self.assertIsInstance(results, tuple)
		self.assertEqual(len(results), 2)
		self.assertIsInstance(results[0], str)
		self.assertIsInstance(results[1], str)
		self.assertTrue(output_path.exists())
	
	def test__get_selected_objects(self):
		objects = ak.wwise.ui.get_selected_objects(platform="Windows", language="English(US)")
		self.assertIsNotNone(objects)
		self.assertGreaterEqual(len(objects), 1)
		self.assertEqual(len(objects[0].other), 0)  # guid, name, type, path, {}
		print(objects)
		return_options = {EReturnOptions.WORK_UNIT, EReturnOptions.TYPE}
		objects = ak.wwise.ui.get_selected_objects(return_options, "Windows", "English(US)")
		self.assertIsNotNone(objects)
		self.assertGreaterEqual(len(objects), 1)
		self.assertEqual(len(objects[0].other), 1)  # guid, name, type, path, {work_unit}
		print(objects)
	
	def test__selection_changed(self):
		def _(objects):
			print(objects)
		ak.wwise.ui.selection_changed += _
		self.assertEqual(len(ak.wwise.ui.selection_changed), 1)
		import time
		time.sleep(30)


if __name__ == '__main__':
	unittest.main()
