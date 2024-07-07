from waapi import WaapiClient as _WaapiClient
from simplevent import RefEvent as _RefEvent


class SoundBank:
	"""ak.wwise.core.soundbank"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
	
		# TODO: implement topics
		self.generated: _RefEvent
		self.generation_done: _RefEvent
	
	def convert_external_sources(self):
		"""
		Converts the external sources files for the project as detailed in the wsources file, and places
		them into either the default folder, or the folder specified by the output argument. External
		Sources are a special type of source that you can put in a Sound object in Wwise. It indicates
		that the real sound data will be provided at run time. While External Source conversion is also
		triggered by SoundBank generation, this operation can be used to process sources not contained in
		the Wwise Project. Please refer to Wwise SDK help page "Integrating External Sources".
		"""
	
	def generate(self):
		"""
		Generate a list of SoundBanks with the import definition specified in the WAAPI request. If you
		do not write the SoundBanks to disk, subscribe to `ak.wwise.core.soundbank.generated` to receive
		SoundBank structure info and the bank data as base64. Note: This is a synchronous operation.
		"""
	
	def get_inclusions(self):
		"""
		Retrieves a SoundBank's inclusion list.
		"""
	
	def process_definition_files(self):
		"""
		Imports SoundBank definitions from the specified file. Multiple files can be specified. See the
		WAAPI log for status messages.
		"""
	
	def set_inclusions(self):
		"""
		Modifies a SoundBank's inclusion list. The 'operation' argument determines how the 'inclusions'
		argument modifies the SoundBank's inclusion list; 'inclusions' may be added to / removed from /
		replace the SoundBank's inclusion list.
		"""
