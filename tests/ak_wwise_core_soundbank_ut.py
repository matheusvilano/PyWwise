import unittest
import pywwise
from pywwise.types import SystemPath as _SystemPath

ak = pywwise.new()

class AkWwiseCoreSoundbankTest(unittest.TestCase):

	def test__convert_external_sources(self):
		pass
	
	def test__generate(self):
		pass
	
	def test__get_inclusions(self):
		pass
	
	def test__process_definition_files(self):
		paths = list[_SystemPath(r"C:/Users/hojun/Documents/SoundBank_DefinitionFile_Test.tsv")]
		results = ak.wwise.core.soundbank.process_definition_files(paths)
		self.assertIsNotNone(results)
	
	def test__set_inclusions(self):
		pass
	