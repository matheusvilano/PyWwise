# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient
from pywwise.ak.wwise.core.audio import Audio as _Audio
from pywwise.ak.wwise.core.audio_source_peaks import AudioSourcePeaks as _AudioSourcePeaks
from pywwise.ak.wwise.core.log import Log as _Log
from pywwise.ak.wwise.core.object import Object as _Object
from pywwise.ak.wwise.core.project import Project as _Project
from pywwise.ak.wwise.core.profiler import Profiler as _Profiler
from pywwise.ak.wwise.core.remote import Remote as _Remote
from pywwise.ak.wwise.core.sound import Sound as _Sound
from pywwise.ak.wwise.core.soundbank import SoundBank as _SoundBank
from pywwise.ak.wwise.core.source_control import SourceControl as _SourceControl
from pywwise.ak.wwise.core.switch_container import SwitchContainer as _SwitchContainer
from pywwise.ak.wwise.core.transport import Transport as _Transport
from pywwise.ak.wwise.core.undo import Undo as _Undo
from pywwise.structs import WwiseObjectWatch


class Core:
	"""ak.wwise.core"""
	
	def __init__(self, client: _WaapiClient, watch_list: tuple[WwiseObjectWatch, ...] = ()):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		:param watch_list: A tuple of `WwiseObjectWatch` instances. This will be used to set up the
						   `ak.wwise.core.object.property_changed` event.
		"""
		self._client = client
		self.audio = _Audio(client)
		self.audio_source_peaks = _AudioSourcePeaks(client)
		self.log = _Log(client)
		self.object = _Object(client, watch_list)
		self.profiler = _Profiler(client)
		self.project = _Project(client)
		self.remote = _Remote(client)
		self.sound = _Sound(client)
		self.soundbank = _SoundBank(client)
		self.source_control = _SourceControl(client)
		self.switch_container = _SwitchContainer(client)
		self.transport = _Transport(client)
		self.undo = _Undo(client)
	
	def execute_lua_script(self):
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_executeluascript.html \n
		Execute a Lua script. Optionally, specify additional Lua search paths, additional modules,
		and additional Lua scripts to load prior to the main script. The script can return a value. All
		arguments will be passed to the Lua script in the "wa_args" global variable.
		"""
		raise NotImplementedError()
	
	def get_info(self):
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_getinfo.html \n
		Retrieve global Wwise information.
		"""
		raise NotImplementedError()
	
	def get_project_info(self):
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_getprojectinfo.html \n
		Retrieve information about the current project opened, including platforms, languages and project
		directories.
		"""
		raise NotImplementedError()
