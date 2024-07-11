import unittest
import pywwise
from pywwise.enums import *
from pywwise.types import *
from pywwise.structs import *
from constants import *
import time

ak = pywwise.new_connection()


class AkWwiseUiProjectTest(unittest.TestCase):

    def test__close_project_is_open(self):
        result = ak.wwise.ui.project.close(True)
        self.assertTrue(result)

    def test__close_project_is_closed(self):
        result = ak.wwise.ui.project.close(True)
        self.assertFalse(result)

    def test__close_project_show_prompt_to_save(self):
        result = ak.wwise.ui.project.close(False)
        ak.wwise.ui.bring_to_foreground()
        self.assertTrue(result)

    def test__close_project_ignore_prompt_to_save(self):
        result = ak.wwise.ui.project.close(True)
        ak.wwise.ui.bring_to_foreground()
        self.assertTrue(result)

    def test__create_project(self):
        output_path = RESOURCES_PROJECT__PATH / "TestProject01" / "TestProject01.wproj"
        ak.wwise.ui.project.create(output_path, None, None)
        time.sleep(5)
        self.assertTrue(output_path.exists())

    def test__create_project_with_platforms(self):
        output_path = RESOURCES_PROJECT__PATH / "TestProject02" / "TestProject02.wproj"
        pywwise_platform = PlatformInfo(name="PyWwise", base_platform=EBasePlatform.WINDOWS)
        windows_platform = PlatformInfo(name="Windows", base_platform=EBasePlatform.WINDOWS)
        android_platform = PlatformInfo(name="Android", base_platform=EBasePlatform.ANDROID)
        platforms = [pywwise_platform, windows_platform, android_platform]
        ak.wwise.ui.project.create(output_path, platforms, None)
        time.sleep(5)
        self.assertTrue(output_path.exists())

    def test__create_project_with_languages(self):
        output_path = RESOURCES_PROJECT__PATH / "TestProject03" / "TestProject03.wproj"
        languages = ["PyWwise", "English(UK)"]
        ak.wwise.ui.project.create(output_path, None, languages)
        time.sleep(5)
        self.assertTrue(output_path.exists())

    def test__open_project(self):
        result = ak.wwise.ui.project.open(WWISE_PROJECT__PATH, False)
        self.assertTrue(result)
        result = ak.wwise.ui.project.open(WWISE_PROJECT__PATH / "Fake", False)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
