import unittest
import pywwise
from pywwise.enums import *
from constants import *


ak = pywwise.new()


class SoundEngineTest(unittest.TestCase):
	
	def test__load_bank(self):
		results = ak.soundengine.load_bank(SOUNDBANK__GUID)
		self.assertTrue(results)
		
	def test__register_game_obj(self):
		results = ak.soundengine.register_game_obj(1, "GameObject_Test_1")
		self.assertTrue(results)
	
	def test__execute_action_on_event(self):
		results = ak.soundengine.execute_action_on_event(EVENT__NAME, EAkActionOnEventType.STOP, GameObjectID.get_transport())
		self.assertIsInstance(results, dict)
		
	def test__get_state(self):
		results = ak.soundengine.get_state(STATE_GROUP__NAME)
		self.assertIsInstance(results, tuple)
		self.assertEqual(len(results), 2)
		self.assertIsInstance(results[0], str)
		self.assertIsInstance(results[1], str)
		
	def test__get_switch(self):
		results = ak.soundengine.get_switch(SWITCH_GROUP__GUID, GameObjectID.get_transport())
		self.assertIsInstance(results, tuple)
		self.assertEqual(len(results), 2)
		self.assertIsInstance(results[0], str)
		self.assertIsInstance(results[1], str)
		
	def test__post_event(self):
		results = ak.soundengine.post_event(EVENT__NAME)
		self.assertIsInstance(results, int)
		self.assertGreaterEqual(results, 0)
		
	def test__post_msg_monitor(self):
		results = ak.soundengine.post_msg_monitor("Message")
		self.assertTrue(results)
		
	def test__post_trigger(self):
		results = ak.soundengine.post_trigger(TRIGGER__GUID)
		self.assertTrue(results)
		results = ak.soundengine.post_trigger(TRIGGER__GUID, GameObjectID.get_transport())
		self.assertTrue(results)
		
	def test__reset_rtpc_value(self):
		results = ak.soundengine.reset_rtpc_value(GAME_PARAMETER__GUID, GameObjectID.get_transport())
		self.assertTrue(results)
		results = ak.soundengine.reset_rtpc_value(GAME_PARAMETER__GUID, GameObjectID.get_global())
		self.assertTrue(results)
	
	def test__seek_on_event(self):
		results = ak.soundengine.seek_on_event(EVENT__GUID)
		self.assertTrue(results)
		
	def test__set_default_listeners(self):
		results = ak.soundengine.set_default_listeners({1})
		self.assertTrue(results)
	
	def test__unload_bank(self):
		results = ak.soundengine.unload_bank(SOUNDBANK__GUID)
		self.assertTrue(results)


if __name__ == '__main__':
	unittest.main()
