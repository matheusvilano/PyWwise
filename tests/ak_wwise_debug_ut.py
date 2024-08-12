import unittest

import pywwise
from constants import *

ak = pywwise.new_waapi_connection()


class AkWwiseDebugTest(unittest.TestCase):
	
	def test__generate_tone_wav(self):
		path = SystemPath("C:/Users/matheusvilano/Documents/Test.wav")
		results = ak.wwise.debug.generate_tone_wav(path)
		self.assertTrue(results)
		self.assertTrue(path.exists())
	
	def test__enable_asserts(self):
		self.assertFalse(ak.wwise.debug.enable_asserts(True))  # not using a build, so this should return False
	
	def test__enable_automation_mode(self):
		self.assertTrue(ak.wwise.debug.enable_automation_mode(True))
	
	def test__get_wal_tree(self):
		self.assertTrue("nodes" in ak.wwise.debug.get_wal_tree())
	
	def test__restart_waapi_servers(self):
		self.assertTrue(ak.wwise.debug.restart_waapi_servers())
	
	def test__test_assert(self):
		self.assertFalse(ak.wwise.debug.test_assert())  # not using a build, so this should return False
	
	def test__test_crash(self):
		self.assertFalse(ak.wwise.debug.test_crash())  # not using a build, so this should return False


if __name__ == '__main__':
	unittest.main()
