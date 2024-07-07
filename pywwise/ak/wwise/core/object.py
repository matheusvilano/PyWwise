from waapi import WaapiClient as _WaapiClient
from simplevent import RefEvent as _RefEvent


class Object:
	"""ak.wwise.core.object"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
		
		# TODO: implement topics
		self._attenuation_curve_changed: _RefEvent
		self._attenuation_curve_link_changed: _RefEvent
		self._child_added: _RefEvent
		self._child_added: _RefEvent
		self._child_removed: _RefEvent
		self._created: _RefEvent
		self._curve_changed: _RefEvent
		self._name_changed: _RefEvent
		self._notes_changed: _RefEvent
		self._post_deleted: _RefEvent
		self._pre_deleted: _RefEvent
		self._property_changed: _RefEvent
		self._reference_changed: _RefEvent
	
	def copy(self):
		"""
		Copies an object to the given parent. Note that if a Work Unit is copied, the operation cannot be
		undone and the project will be saved.
		"""
	
	def create(self):
		"""
		Creates an object of type 'type', as a child of 'parent'. Refer to Importing Audio Files and
		Creating Structures for more information about creating objects. Also refer to
		`ak.wwise.core.audio.import_files` to import audio files to Wwise. To create Effect or Source
		plug-ins, use `ak.wwise.core.object.set`, and refer to Wwise Objects Reference for the classId.
		"""
	
	def delete(self):
		"""
		Deletes the specified object. Note that if a Work Unit is deleted, the operation cannot be undone
		and the project will be saved.
		"""
	
	def diff(self):
		"""
		Compares properties and lists of the source object with those in the target object.
		"""
	
	def get(self):
		"""
		Performs a query and returns the data, as specified in the options, for each object in the query
		result. The query can specify either a 'waql' argument or a 'from' argument with an optional
		'transform' argument. Refer to Using the Wwise Authoring Query Language (WAQL) or Querying the
		Wwise Project for more information. Refer to Return Options to learn about options.
		"""
	
	def get_attenuation_curve(self):
		"""
		Gets the specified attenuation curve for a given attenuation object.
		"""
	
	def get_property_and_reference_names(self):
		"""
		Retrieves the list of property and reference names for an object.
		"""
	
	def get_property_info(self):
		"""
		Retrieves information about an object property. Note that this function does not return the value
		of a property. To retrieve the value of a property, refer to `ak.wwise.core.object.get` and Return
		Options.
		"""
	
	def get_types(self):
		"""
		Retrieves the list of all object types registered in Wwise's object model. This function returns
		the equivalent of Wwise Objects Reference.
		"""
	
	def is_linked(self):
		"""
		Indicates whether a property, reference, or object list is bound to a particular platform or to
		all platforms.
		"""
	
	def is_property_enabled(self):
		"""
		Returns true if a property is enabled based on the values of the properties it depends on.
		"""
	
	def move(self):
		"""
		Moves an object to the given parent. Returns the moved object.
		"""
	
	def paste_properties(self):
		"""
		Pastes properties, references and lists from one object to any number of target objects. Only
		those properties, references and lists which differ between source and target are pasted. Refer
		to Wwise Objects Reference for more information on the properties, references and lists available
		on each object type.
		"""
	
	def set(self):
		"""
		Allows for batch processing of the following operations: Object creation in a child hierarchy,
		Object creation in a list, Setting name, notes, properties and references. Refer to Importing
		Audio Files and Creating Structures for more information about creating objects. Also refer to
		`ak.wwise.core.audio.import_files` to import audio files to Wwise.
		"""
	
	def set_attenuation_curve(self):
		"""
		Sets the specified attenuation curve for a given attenuation object.
		"""
	
	def set_linked(self):
		"""
		Link or unlink a property/reference or object list to a particular platform.
		"""
	
	def set_name(self):
		"""
		Renames an object.
		"""
	
	def set_notes(self):
		"""
		Sets the object's notes.
		"""
	
	def set_property(self):
		"""
		Sets a property value of an object for a specific platform. Refer to Wwise Objects Reference for
		more information on the properties available on each object type. Refer to
		`ak.wwise.core.object.set_reference` to set a reference to an object. Refer to
		`ak.wwise.core.object.get` to obtain the value of a property for an object.
		"""
	
	def set_randomizer(self):
		"""
		Sets the randomizer values of a property of an object for a specific platform. Refer to Wwise
		Objects Reference for more information on the properties available on each object type.
		"""
	
	def set_reference(self):
		"""
		Sets an object's reference value. Refer to Wwise Objects Reference for more information on the
		references available on each object type.
		"""
	
	def set_state_groups(self):
		"""
		Sets the State Group objects associated with an object. Note, this will remove any previously
		associated State Group.
		"""
	
	def set_state_properties(self):
		"""
		Set the state properties of an object. Note, this will remove any previous state property,
		including the default ones.
		"""
