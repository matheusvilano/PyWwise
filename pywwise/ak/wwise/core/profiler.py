from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient
from pywwise.ak.wwise.core.capture_log import CaptureLog as _CaptureLog


class Profiler:
	"""ak.wwise.core.profiler"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
		self.capture_log = _CaptureLog(client)
		
		# TODO: implement topics
		self.game_object_registered: _RefEvent
		self.game_object_reset: _RefEvent
		self.game_object_unregistered: _RefEvent
		self.state_changed: _RefEvent
		self.switch_changed: _RefEvent
	
	def enable_profiler_data(self):
		"""
		Specifies the type of data you want to capture. Overrides the user's profiler settings.
		"""
	
	def get_audio_objects(self):
		"""
		Retrieves the Audio Objects at a specific profiler capture time.
		"""
	
	def get_busses(self):
		"""
		Retrieves the busses at a specific profiler capture time.
		"""
	
	def get_cpu_usage(self):
		"""
		Retrieves CPU usage statistics at a specific profiler capture time. This data can also be found
		in the Advanced Profiler, under the CPU tab. To ensure the CPU data is received,
		refer to `ak.wwise.core.profiler.enable_profiler_data`. The returned data includes "Inclusive" and
		"Exclusive" values, where "Inclusive" refers to the time spent in the element plus the time spent
		in any called elements, and "Exclusive" values pertain to execution only within the element
		itself.
		"""
	
	def get_cursor_time(self):
		"""
		Returns the current time of the specified profiler cursor, in milliseconds.
		"""
	
	def get_game_objects(self):
		"""
		Retrieves the game objects at a specific profiler capture time.
		"""
	
	def get_loaded_media(self):
		"""
		Retrieves the loaded media at a specific profiler capture time. This data can also be found in
		the Advanced Profiler, under the Loaded Media tab. To ensure the Loaded Media data is received,
		refer to `ak.wwise.core.profiler.enable_profiler_data`.
		"""
	
	def get_performance_monitor(self):
		"""
		Retrieves the Performance Monitor statistics at a specific profiler capture time. Refer to Wwise
		Authoring Performance Monitor Counter Identifiers for the available counters.
		"""
	
	def get_rtpcs(self):
		"""
		Retrieves active RTPCs at a specific profiler capture time.
		"""
	
	def get_streamed_media(self):
		"""
		Retrieves the streaming media at a specific profiler capture time. This data can also be found in
		the Advanced Profiler, under the Streams tab. To ensure the Streams data is received,
		refer to `ak.wwise.core.profiler.enable_profiler_data`.
		"""
	
	def get_voice_contributions(self):
		"""
		Retrieves all parameters affecting voice volume, highpass and lowpass for a voice path,
		resolved from pipeline IDs.
		"""
	
	def get_voices(self):
		"""
		Retrieves the voices at a specific profiler capture time.
		"""
	
	def save_capture(self):
		"""
		Saves profiler as a .prof file according to the given file path.
		"""
	
	def start_capture(self):
		"""
		Starts the profiler capture and returns the time at the beginning of the capture, in milliseconds.
		"""
	
	def stop_capture(self):
		"""
		Stops the profiler capture and returns the time at the end of the capture, in milliseconds.
		"""
