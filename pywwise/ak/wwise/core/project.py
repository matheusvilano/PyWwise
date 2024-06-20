from waapi import WaapiClient as _WaapiClient


class Project:
	"""ak.wwise.core.project"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
	
	def save(self):
		"""
		Saves the current project.
		"""
