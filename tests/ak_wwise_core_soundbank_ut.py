import unittest
import pywwise
from pywwise.enums import *
from pywwise.types import *
from pywwise.structs import *
from constants import *

ak = pywwise.new()


class AkWwiseCoreSoundbankTest(unittest.TestCase):

	def test__convert_external_sources(self):
		paths = list(SystemPath.glob(WAVE_ASSET__PATH))
		results = ak.wwise.core.soundbank.convert_external_sources(paths)
		self.assertIsNotNone(results)
	
	def test__generate(self):
		sound_bank_list = [{"name": SOUNDBANK__NAME}]
		results = ak.wwise.core.soundbank.generate(sound_bank_list)
		self.assertIsNotNone(results)
	
	def test__get_inclusions(self):
		results = ak.wwise.core.soundbank.get_inclusions(SOUNDBANK__GUID)
		self.assertIsNotNone(results)
	
	def test__process_definition_files(self):
		paths = list(DEFINITION_TSV__PATH)
		results = ak.wwise.core.soundbank.process_definition_files(paths)
		self.assertIsNotNone(results)
	
	def test__set_inclusions(self):
		soundbank = SOUNDBANK__GUID
		operation = EInclusionOperation.ADD
		inclusions = (SoundBankInclusion(EVENT__GUID, [EInclusionFilter.EVENTS, EInclusionFilter.STRUCTURES, EInclusionFilter.MEDIA]),)
		results = ak.wwise.core.soundbank.set_inclusions(soundbank, operation,
		                                                 inclusions)
		self.assertIsNotNone(results)
