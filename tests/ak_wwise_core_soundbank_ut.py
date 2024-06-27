import unittest
import pywwise
from pywwise.types import SystemPath

ak = pywwise.new()

class AkWwiseCoreSoundbankTest(unittest.TestCase):

    def test_convert_external_sources(self):
        pass

    def test__generate(self):
        pass

    def test__get_inclusions(self):
        pass
    
    def test__process_definition_files(self):
        ak = pywwise.new()
        path = SystemPath("C:/Users/hojun/Documents/SoundBank_DefinitionFile_Test.csv")
        results = ak.wwise.core.soundbank.process_definition_files(path)
        self.assertTrue(results)

    def test__set_inclusions(self):
        pass


if __name__ == '__main__':
    unittest.main()
    