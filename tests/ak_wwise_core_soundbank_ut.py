import unittest
import pywwise

ak = pywwise.new()

class AkWwiseCoreSoundbankTest(unittest.TestCase):

    # def test_convert_external_sources(self):
    #
    #
    # def test__generate(self):
    #
    #
    # def test__get_inclusions(self):


    def test__process_definition_files(self):
        import pathlib
        path = pathlib.Path("C:/Users/hojun/Documents/SoundBank_DefinitionFile_Test.txt")
        results = ak.wwise.core.soundbank.process_definition_files(path)
        self.assertTrue(results)

    # def test__set_inclusions(self):



if __name__ == '__main__':
        unittest.main()