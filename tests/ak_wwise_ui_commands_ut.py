import unittest
import time
import pywwise
from pywwise.enums import *
from pywwise.types import *
from pywwise.structs import *
from constants import *

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
		result = ak.wwise.ui.commands.execute("GenerateAllSoundbanksCurrentPlatformAutoClose", None,
		                                      {GUID("{2DD3590C-441E-4896-A802-77C4EF7EAD5C}")})
		self.assertIsNotNone(result)
		result = ak.wwise.ui.commands.execute("GenerateAllSoundbanksCurrentPlatformAutoClose", None)
		self.assertIsNotNone(result)
		result = ak.wwise.ui.commands.execute("Search", None, None, "SoundVoice_Test")
		self.assertIsNotNone(result)
	
	def test__register(self):
		context_menu = ContextMenuInfo(base_path="Editors", enabled_for={EObjectType.SOUND, EObjectType.WORK_UNIT})
		main_menu = MainMenuInfo(main_menu_base_path="Extra")
		open_in_vscode = CommandInfo(id="ak.edit_in_vscode", display_name="Edit in Visual Studio Code",
		                             default_shortcut="C", program="Code",
		                             start_mode=EStartMode.MULTIPLE_SELECTION_SINGLE_PROCESS_SPACE_SEPARATED,
		                             args="${filePath}", cwd=None, context_menu=context_menu, main_menu=main_menu)
		result = ak.wwise.ui.commands.register({open_in_vscode})
		self.assertIsNotNone(result)
	
	def test__unregister(self):
		result = ak.wwise.ui.commands.unregister({"ak.edit_in_vscode"})
		self.assertIsNotNone(result)
	
	def test__executed(self):
		def _print(command, objects, platforms):
			print(f"{command}\n{objects}\n{platforms}")
		
		ak.wwise.ui.commands.executed += _print
		self.assertEqual(len(ak.wwise.ui.commands.executed), 1)
		time.sleep(10)


if __name__ == '__main__':
	unittest.main()
