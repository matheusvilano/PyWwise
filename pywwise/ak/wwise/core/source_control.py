from waapi import WaapiClient as _WaapiClient


class SourceControl:
	"""ak.wwise.core.sourceControl"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
	
	def add(self):
		"""
		Add files to source control. Equivalent to Mark for Add for Perforce.
		"""
	
	def check_out(self):
		"""
		Check out files from source control. Equivalent to Check Out for Perforce.
		"""
	
	def commit(self):
		"""
		Commit files to source control. Equivalent to Submit Changes for Perforce.
		"""
	
	def delete(self):
		"""
		Delete files from source control. Equivalent to Mark for Delete for Perforce.
		"""
	
	def get_source_files(self):
		"""
		Retrieve all original files.
		"""
	
	def get_status(self):
		"""
		Get the source control status of the specified files.
		"""
	
	def move(self):
		"""
		Move or rename files in source control. Always pass the same number of elements in files and
		newFiles. Equivalent to Move for Perforce.
		"""
	
	def revert(self):
		"""
		Revert changes to files in source control.
		"""
	
	def set_provider(self):
		"""
		Change the source control provider and credentials. This is the same setting as the Source
		Control option in the Project Settings dialog in Wwise.
		"""
