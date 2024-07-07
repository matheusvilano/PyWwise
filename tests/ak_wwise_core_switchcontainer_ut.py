from unittest import main

from constants import *
from testclass import PyWwiseTest


class AkWwiseCoreSwitchContainerTest(PyWwiseTest):
	"""Unit tests for `ak.wwise.core.switch_container`."""
	
	def test__add_assignment(self):
		results = self.ak.wwise.core.switch_container.add_assignment(GUID("{704FA742-B41E-46EC-BAB3-97EFB55D2288}"),
		                                                             GUID("{05D0A833-9359-4E25-8F8E-2E1D413616D7}"))
		self.assertIsNotNone(results)
	
	def test__get_assignments(self):
		results = self.ak.wwise.core.switch_container.get_assignments(SWITCH_CONTAINER__PATH)
		self.assertIsNotNone(results)
		self.assertIsInstance(results, tuple)
	
	def test__remove_assignment(self):
		results = self.ak.wwise.core.switch_container.remove_assignment(GUID("{704FA742-B41E-46EC-BAB3-97EFB55D2288}"),
		                                                                GUID("{05D0A833-9359-4E25-8F8E-2E1D413616D7}"))
		self.assertIsNotNone(results)


if __name__ == '__main__':
	main()
