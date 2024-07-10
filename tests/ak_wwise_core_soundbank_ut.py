import unittest
import pywwise
from pywwise.types import SystemPath

ak = pywwise.new()


class AkWwiseCoreSoundbankTest(unittest.TestCase):

	def test__convert_external_sources(self):
		paths = list(SystemPath.glob(r"C:\Users\hojun\Documents\PyWwiseTestMaterials\ExternalSourceFiles\BottleOpen.wav",
		                             r"C:\Users\hojun\Documents\PyWwiseTestMaterials\ExternalSourceFiles\GlassMarbleDrop.wav"))
		results = ak.wwise.core.soundbank.convert_external_sources(paths)
		self.assertIsNotNone(results)
	
	def test__generate(self):
		sound_bank_list = [r"\SoundBanks\Default Work Unit\SoundBank_Test"]
		results = ak.wwise.core.soundbank.generate(sound_bank_list)
		self.assertIsNotNone(results)
	
	def test__get_inclusions(self):
		sound_bank = r"\SoundBanks\Default Work Unit\SoundBank_Test"
		results = ak.wwise.core.soundbank.get_inclusions(sound_bank)
		self.assertIsNotNone(results)
	
	def test__process_definition_files(self):
		paths = list(SystemPath.glob(r"C:\Users\hojun\Documents\PyWwiseTestMaterials\SoundBank_DefinitionFile_Test.tsv"))
		results = ak.wwise.core.soundbank.process_definition_files(paths)
		self.assertIsNotNone(results)
	
	def test__set_inclusions(self):
		sound_bank = r"\SoundBanks\Default Work Unit\SoundBank_Test"
		operation = "add"
		inclusions = [{"Event:Event_Test": "event"}]
		results = ak.wwise.core.soundbank.set_inclusions(sound_bank, operation,
		                                                 inclusions)
		self.assertIsNotNone(results)
