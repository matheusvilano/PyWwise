from waapi import WaapiClient as _WaapiClient


class SwitchContainer:
	"""ak.wwise.core.switchContainer"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
	
	def add_assignment(self):
		"""
		Assigns a Switch Container's child to a Switch. This is the equivalent of doing a drag&drop of
		the child to a state in the Assigned Objects view. The child is always added at the end for each
		state.
		"""
	
	def get_assignments(self):
		"""
		Returns the list of assignments between a Switch Container's children and states.
		"""
	
	def remove_assignment(self):
		"""
		Removes an assignment between a Switch Container's child and a State.
		"""
