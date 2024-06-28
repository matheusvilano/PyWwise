from waapi import WaapiClient as _WaapiClient
from simplevent import RefEvent as _RefEvent
from pywwise.types import SystemPath
from pywwise.enums import EBitDepth, ESampleRate, ESpeakerBitMask, EWaveform
from pywwise.decorators import callback, debug_build_only


class Debug:
	"""ak.wwise.debug"""
	
	def __init__(self, client: _WaapiClient, is_debug_build: bool = False):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		:param is_debug_build: Should be set to true if the instance of Wwise is a debug build and debug-only
		functions/topics are required.
		"""
		self._client = client
		
		self._is_debug_build = is_debug_build
		
		self.assert_failed = _RefEvent(str, str, int, str, str)
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_debug_assertfailed.html
		\nSent when an assert has failed. **This is only available in Debug builds**.
		\n**Event Data**
		\n- The expression that failed.
		\n- The name of the source file.
		\n- The line number.
		\n- The callstack from the location of the assert.
		\n- An explanatory message accompanying the assert. May be empty.
		"""
		
		if self._is_debug_build:
			self._assert_failed = self._client.subscribe("ak.wwise.debug.assertFailed", self._on_assert_failed)
	
	@callback
	def _on_assert_failed(self, **kwargs):
		"""
		Callback function for the `assertFailed` event.
		:param kwargs: The event data.
		"""
		self.assert_failed(kwargs["expression"], kwargs["fileName"], int(kwargs["lineNumber"]),
		                   kwargs["callstack"], kwargs.get("message", ""))
	
	@debug_build_only
	def enable_asserts(self, enable: bool):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_debug_enableasserts.html \n
		Enables debug assertions. Every call to enableAsserts with 'false' increments the ref count. Calling
		with true decrements the ref count. **This is only available with Debug builds**.
		:param enable: Whether to enable debug assertions.
		:return: Whether the call succeeded.
		"""
		return self._client.call("ak.wwise.debug.enableAsserts", {"enable": enable})
	
	def enable_automation_mode(self, enable: bool):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_debug_enableautomationmode.html \n
		Enables or disables the automation mode for Wwise. This reduces the potential interruptions caused by
		message boxes and dialogs. For instance, enabling the automation mode silently accepts: project
		migration, project load log, EULA acceptance, project licence display and generic message boxes.
		:param enable: Whether to enable automation mode.
		:return: Whether the call succeeded.
		"""
	
	def generate_tone_wav(self, path: SystemPath, bit_depth: EBitDepth = EBitDepth.INT_16,
	                      sample_rate: ESampleRate = ESampleRate.SR_44100,
	                      channel_config: ESpeakerBitMask = ESpeakerBitMask.MONO, attack_time: float = 0.0,
	                      sustain_time: float = 1.0, sustain_level: float = 0.0, release_time: float = 0.0,
	                      waveform: EWaveform = EWaveform.SILENCE, frequency: float = 440.0):
		"""
		Generate a WAV file playing a tone with a simple envelope and save it to the specified location. This
		is provided as a utility to generate test WAV files.
		:param path: The path where to store the generated WAV file.
		:param bit_depth: The bit depth of the new audio file.
		:param sample_rate: The sample rate of the new audio file.
		:param channel_config: The channel configuration of the new audio file.
		:param attack_time: The attack time of the sound to generate.
		:param sustain_time: The sustain time of the sound to generate.
		:param sustain_level: The sustain level of the sound to generate. This is clamped to the range [-100.0, 0.0].
		:param release_time: The release time of the sound to generate.
		:param waveform: The waveform of the sound to generate.
		:param frequency: The frequency of the sound to generate. This is clamped to the range [1.0, 22000.0].
		:return: Whether the call succeeded. Although True means the file likely got generated successfully, it is not
		a guarantee.
		"""
		args = {"path": str(path), "bitDepth": bit_depth.value, "sampleRate": sample_rate.value,
		        "channelConfig": channel_config.get_name(), "attackTime": attack_time,
		        "sustainTime": sustain_time, "sustainLevel": max(-100.0, min(sustain_level, 0.0)),
		        "releaseTime": release_time, "waveform": waveform.value, "frequency": max(1.0, min(frequency, 22000.0))}
		return self._client.call("ak.wwise.debug.generateToneWAV", args) is not None
	
	def get_wal_tree(self):
		"""
		Retrieves the WAL tree, which describes the nodes that are synchronized in the Sound Engine. Private
		use only.
		"""
	
	def restart_waapi_servers(self):
		"""
		Restart WAAPI servers. For internal use only.
		"""
	
	def test_assert(self):
		"""
		Private use only.
		"""
	
	def test_crash(self):
		"""
		Private use only.
		"""
