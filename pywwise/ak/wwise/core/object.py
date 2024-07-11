from waapi import WaapiClient as _WaapiClient
from simplevent import RefEvent as _RefEvent
from pywwise.decorators import callback
from pywwise.enums import EAttenuationCurveType, EObjectType, EReturnOptions
from pywwise.statics import EnumStatics
from pywwise.structs import WwiseObjectInfo
from pywwise.types import GUID, Name, ProjectPath


class Object:
	"""ak.wwise.core.object"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
		
		return_options = {"return": [EReturnOptions.GUID, EReturnOptions.NAME,
		                             EReturnOptions.TYPE, EReturnOptions.PATH]}
		
		self.attenuation_curve_changed = _RefEvent(WwiseObjectInfo, EAttenuationCurveType)
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_object_attenuationcurvechanged.html
		\nSent when an attenuation curve is changed.
		\n**Event Data**:
		\n- A WwiseObjectInfo instance representing the Attenuation object that owns the curve.
		\n- The type of the curve that changed.
		"""
		
		self._attenuation_curve_changed = self._client.subscribe(
			"ak.wwise.core.object.attenuationCurveChanged",
			self._on_attenuation_curve_changed, return_options)
		
		self.attenuation_curve_link_changed = _RefEvent(WwiseObjectInfo, EAttenuationCurveType)
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_object_attenuationcurvelinkchanged.html
		\nSent when an attenuation curve's link/unlink is changed. NOTE: this event often multi-triggers.
		\n**Event Data**:
		\n- A WwiseObjectInfo instance representing the Attenuation object that owns the curve.
		\n- The type of the curve that had its link changed.
		"""
		
		self._attenuation_curve_link_changed = self._client.subscribe(
			"ak.wwise.core.object.attenuationCurveLinkChanged",
			self._on_attenuation_curve_link_changed, return_options)
		
		self.child_added = _RefEvent(WwiseObjectInfo, WwiseObjectInfo)
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_object_childadded.html
		\nSent when an object is added as a child to another object.
		\n*Event Data**:
		\n- A WwiseObjectInfo instance representing the new child object.
		\n- A WwiseObjectInfo instance representing the parent of the new child object.
		"""
		
		self._child_added = self._client.subscribe("ak.wwise.core.object.childAdded",
		                                           self._on_child_added, return_options)
		
		self.child_removed = _RefEvent(WwiseObjectInfo, WwiseObjectInfo)
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_object_childadded.html
		\nSent when an object is removed from the children of another object.
		\n*Event Data**:
		\n- A WwiseObjectInfo instance representing the child object that got removed.
		\n- A WwiseObjectInfo instance representing the former parent of the child object.
		"""
		
		self._child_removed = self._client.subscribe("ak.wwise.core.object.childRemoved",
		                                             self._on_child_removed, return_options)
		
		self.created = _RefEvent(WwiseObjectInfo)
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_object_created.html
		\nSent when an object is created. Includes Object Setting Associations, which do not have valid paths or names.
		\n**Event Data**:
		\n- A WwiseObjectInfo instance representing the newly created object.
		"""
		
		self._created = self._client.subscribe("ak.wwise.core.object.created",
		                                       self._on_created, return_options)
		
		# TODO: implement topics
		self.curve_changed: _RefEvent
		self.name_changed: _RefEvent
		self.notes_changed: _RefEvent
		self.post_deleted: _RefEvent
		self.pre_deleted: _RefEvent
		self.property_changed: _RefEvent
		self.reference_changed: _RefEvent
	
	@callback
	def _on_attenuation_curve_changed(self, event, **kwargs):
		"""
		Callback function for the `attenuationCurveChanged` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		event(*self._on_attenuation_event(**kwargs))
	
	@callback
	def _on_attenuation_curve_link_changed(self, event, **kwargs):
		"""
		Callback function for the `attenuationCurveLinkChanged` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		event(*self._on_attenuation_event(**kwargs))
	
	@staticmethod
	def _on_attenuation_event(**kwargs) -> tuple[WwiseObjectInfo, EAttenuationCurveType]:
		"""
		Utility function for the `attenuationCurveChanged` and `attenuationCurveLinkChanged` events.
		:param kwargs: The event data.
		:return: The event data, processed.
		"""
		attenuation = kwargs["attenuation"]
		info = WwiseObjectInfo(GUID(attenuation["id"]),
		                       Name(attenuation["name"]),
		                       EObjectType.from_type_name(attenuation["type"]),
		                       ProjectPath(attenuation["path"]))
		curve = EnumStatics.from_value(EAttenuationCurveType, kwargs["curveType"])
		return info, curve
	
	@callback
	def _on_child_added(self, event, **kwargs):
		"""
		Callback function for the `childAdded` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		event(*self._on_child_event(**kwargs))
		
	@callback
	def _on_child_removed(self, event, **kwargs):
		"""
		Callback function for the `childRemoved` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		event(*self._on_child_event(**kwargs))
	
	@staticmethod
	def _on_child_event(**kwargs) -> tuple[WwiseObjectInfo, WwiseObjectInfo]:
		"""
		Utility function for the `childAdded` and `childRemoved` events.
		:param kwargs: The event data.
		:return: The event data, processed.
		"""
		child = kwargs["child"]
		child = WwiseObjectInfo(GUID(child["id"]),
		                        Name(child["name"]),
		                        EObjectType.from_type_name(child["type"]),
		                        ProjectPath(child["path"]))
		parent = kwargs["parent"]
		parent = WwiseObjectInfo(GUID(parent["id"]),
		                         Name(parent["name"]),
		                         EObjectType.from_type_name(parent["type"]),
		                         ProjectPath(parent["path"]))
		return child, parent
	
	@callback
	def _on_created(self, event, **kwargs):
		"""
		Callback function for the `created` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		obj = kwargs["object"]
		event(WwiseObjectInfo(GUID(obj["id"]),
		                      Name(obj["name"] if obj["name"] != "" else Name.get_null()),
		                      EObjectType.from_type_name(obj["type"]),
		                      ProjectPath))
	
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
