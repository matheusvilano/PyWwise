from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient

from pywwise.decorators import callback
from pywwise.types import SystemPath


class Project:
	"""ak.wwise.core.project"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
		
		self.saved = _RefEvent(tuple[SystemPath, ...])
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_project_saved.html
		\nSent when the project has been saved.
		\n**Event Data**:
		\n- A tuple containing the absolute paths to the Work Unit and Project files that were modified.
		"""
		
		self._saved = self._client.subscribe("ak.wwise.core.project.saved", self._on_saved)
		
		# TODO: implement topics
		self.loaded: _RefEvent
		self.post_closed: _RefEvent
		self.pre_closed: _RefEvent
	
	@callback
	def _on_saved(self, **kwargs):
		"""
		Callback function for the `saved` event.
		:param kwargs: The event data.
		"""
		self.saved(tuple(SystemPath(path) for path in kwargs.get("modifiedPaths", dict())))
	
	def save(self, auto_check_out_to_version_control: bool = True) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_project_save.html \n
		Saves the current project.
		:param auto_check_out_to_version_control: Whether to automatically check out changes to version control.
		:return: Whether the operation succeeded.
		"""
		args = {"autoCheckOutToSourceControl": auto_check_out_to_version_control}
		return self._client.call("ak.wwise.core.project.save", args) is not None
