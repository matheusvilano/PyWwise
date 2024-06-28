import unittest
import pywwise
from pywwise.enums import *
from pywwise.types import *
from pywwise.structs import *
from constants import *

ak = pywwise.new()


class AkWwiseDebugTest(unittest.TestCase):
	
	def test__generate_tone_wav(self):
		path = SystemPath("C:/Users/matheusvilano/Documents/Test.wav")
		results = ak.wwise.debug.generate_tone_wav(path)
		self.assertTrue(results)
		self.assertTrue(path.exists())


if __name__ == '__main__':
	unittest.main()
