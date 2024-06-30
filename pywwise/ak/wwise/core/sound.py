from waapi import WaapiClient as _WaapiClient


class Sound:
	"""ak.wwise.core.sound"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
	
	def get_active_source(self):
		"""
		Sets which version of the source is being used for the specified sound. Use
		`ak.wwise.core.object.get` with the 'activeSource' return option to get the active source of a
		sound.
		"""
