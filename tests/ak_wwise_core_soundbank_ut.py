from unittest import TestCase

from constants import *
from pywwise import *

ak = new_waapi_connection()


class AkWwiseCoreSoundbankTest(TestCase):
    
    def test__convert_external_sources(self):
        paths = [ExternalSourceInfo(WAVE_ASSET__PATH, Name("Windows"), None)]
        results = ak.wwise.core.soundbank.convert_external_sources(paths)
        self.assertIsNotNone(results)
    
    def test__generate(self):
        sound_bank_list = [SOUNDBANK__NAME]
        results = ak.wwise.core.soundbank.generate(sound_bank_list)
        self.assertIsNotNone(results)
    
    def test__get_inclusions(self):
        set_waapi_logging(0)
        results = ak.wwise.core.soundbank.get_inclusions(SOUNDBANK__GUID)
        self.assertIsNotNone(results)
    
    def test__process_definition_files(self):
        paths = list[DEFINITION_TSV__PATH]
        results = ak.wwise.core.soundbank.process_definition_files(paths)
        self.assertIsNotNone(results)
    
    def test__set_inclusions(self):
        soundbank = SOUNDBANK__GUID
        operation = EInclusionOperation.ADD
        inclusions = (SoundBankInclusion(EVENT__GUID, [EInclusionFilter.EVENTS, EInclusionFilter.STRUCTURES,
                                                       EInclusionFilter.MEDIA]),)
        results = ak.wwise.core.soundbank.set_inclusions(soundbank, operation, inclusions)
        self.assertIsNotNone(results)
