import unittest
import pywwise
from pywwise.enums import *
from pywwise.types import *
from pywwise.structs import *
from constants import *
import time

ak = pywwise.new()


class AkWwiseUiCommandsTest(unittest.TestCase):

	def test__get_commands(self):
		result = ak.wwise.ui.commands.get_commands()
		self.assertIsInstance(result, list)
		if result is not None:
			for result in result:
				self.assertIsInstance(result, str)

	def test__execute(self):
		objects = {GUID("{2A11A310-B5F5-4CAB-90B9-AA67696D4EB9}"), GUID("{41C1F653-A793-446B-B1DD-1AD2074F06C5}")}
		result = ak.wwise.ui.commands.execute("FindInProjectExplorerSelectionChannel1", objects)
		self.assertIsNotNone(result)
		result = ak.wwise.ui.commands.execute("GenerateAllSoundbanksCurrentPlatformAutoClose", None, {GUID("{2DD3590C-441E-4896-A802-77C4EF7EAD5C}")})
		self.assertIsNotNone(result)
		result = ak.wwise.ui.commands.execute("GenerateAllSoundbanksCurrentPlatformAutoClose", None)
		self.assertIsNotNone(result)
		result = ak.wwise.ui.commands.execute("Search", None, None, "SoundVoice_Test")
		self.assertIsNotNone(result)

	def test__register(self):
		result = ak.wwise.ui.commands.register()
		self.assertIsNone(result)

	def test__unregister(self):
		result = ak.wwise.ui.commands.unregister()
		self.assertIsNone(result)


if __name__ == '__main__':
	unittest.main()
