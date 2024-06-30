from waapi import WaapiClient as _WaapiClient


class Transport:
	"""ak.wwise.core.transport"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
	
	def create(self):
		"""
		Creates a transport object for the given Wwise object. The return transport object can be used to
		play, stop, pause and resume the Wwise object via the other transport functions.
		"""
	
	def destroy(self):
		"""
		Destroys the given transport object.
		"""
	
	def execute_action(self):
		"""
		Executes an action on the given transport object, or all transport objects if none is specified.
		"""
	
	def get_list(self):
		"""
		Returns the list of transport objects.
		"""
	
	def get_state(self):
		"""
		Gets the state of the given transport object.
		"""
	
	def prepare(self):
		"""
		Prepare the object and its dependencies for playback. Use this function before calling
		`PostEventSync` or `PostMIDIOnEventSync` from `IAkGlobalPluginContext`.
		"""
	
	def use_originals(self):
		"""
		Sets the Original/Converted transport toggle globally. This allows playing the original or the
		converted sound files.
		"""
