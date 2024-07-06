import unittest
import pywwise
from pywwise.enums import *
from pywwise.types import *
from pywwise.structs import *
from constants import *

ak = pywwise.new()


class AkWwiseDebugTest(unittest.TestCase):
	def test__save(self):
		self.assertTrue(ak.wwise.core.project.save(False))
		
	def test__saved(self):
		def on_saved(paths: tuple[SystemPath, ...]):
			self.assertIsNotNone(paths)
			self.assertIsInstance(paths, tuple)
			print(f"Project Saved")
			print(f"Paths:\n{paths}")
		ak.wwise.core.project.saved += on_saved
		ak.wwise.core.project.save(False)


if __name__ == '__main__':
	unittest.main()