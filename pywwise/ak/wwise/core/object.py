from typing import Any as _Any
from waapi import WaapiClient as _WaapiClient, EventHandler as _EventHandler
from simplevent import RefEvent as _RefEvent
from pywwise.decorators import callback
from pywwise.enums import (EAttenuationCurveType, EAttenuationCurveUsage, EAttenuationCurveShape, ENameConflictStrategy,
                           EObjectType, EReturnOptions)
from pywwise.statics import EnumStatics
from pywwise.structs import AttenuationCurve, GraphPoint2D, Vector2, WwiseObjectInfo, WwiseObjectWatch
from pywwise.types import GUID, Name, ProjectPath
from pywwise.waql import WAQL


class Object:
	"""ak.wwise.core.object"""
	
	def __init__(self, client: _WaapiClient, watch_list: tuple[WwiseObjectWatch, ...] = ()):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		:param watch_list: A tuple of `WwiseObjectWatch` instances. This will be used to set up the
						   `ak.wwise.core.object.property_changed` event.
		"""
		self._client = client
		
		return_options = {"return": [EReturnOptions.GUID, EReturnOptions.NAME,
		                             EReturnOptions.TYPE, EReturnOptions.PATH]}
		
		self.attenuation_curve_changed = _RefEvent(WwiseObjectInfo, EAttenuationCurveType)
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_attenuationcurvechanged.html
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
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_attenuationcurvelinkchanged.html
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
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_childadded.html
		\nSent when an object is added as a child to another object.
		\n*Event Data**:
		\n- A WwiseObjectInfo instance representing the new child object.
		\n- A WwiseObjectInfo instance representing the parent of the new child object.
		"""
		
		self._child_added = self._client.subscribe("ak.wwise.core.object.childAdded",
		                                           self._on_child_added, return_options)
		
		self.child_removed = _RefEvent(WwiseObjectInfo, WwiseObjectInfo)
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_childadded.html
		\nSent when an object is removed from the children of another object.
		\n*Event Data**:
		\n- A WwiseObjectInfo instance representing the child object that got removed.
		\n- A WwiseObjectInfo instance representing the former parent of the child object.
		"""
		
		self._child_removed = self._client.subscribe("ak.wwise.core.object.childRemoved",
		                                             self._on_child_removed, return_options)
		
		self.created = _RefEvent(WwiseObjectInfo)
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_created.html
		\nSent when an object is created. The name and path are not available at the time of creation.
		\n**Event Data**:
		\n- A WwiseObject instance representing the newly created object.
		"""
		
		self._created = self._client.subscribe("ak.wwise.core.object.created",
		                                       self._on_created, return_options)
		
		self.curve_changed = _RefEvent(WwiseObjectInfo, WwiseObjectInfo)
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_curvechanged.html
		\nSent when one or many curves are changed.
		\n**Event Data**:
		\n- A WwiseObjectInfo instance representing the curve that changed.
		\n- A WwiseObjectInfo instance representing the owner of the curve that changed.
		"""
		
		self._curve_changed = self._client.subscribe("ak.wwise.core.object.curveChanged",
		                                             self._on_curve_changed, return_options)
		
		self.name_changed = _RefEvent(WwiseObjectInfo, str)
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_namechanged.html
		\nSent when an object is renamed. Publishes the renamed object.
		\n**Event Data**:
		\n- A WwiseObjectInfo instance representing the object that was renamed. It will contain the new name.
		\n- A string containing the old name.
		"""
		
		self._name_changed = self._client.subscribe("ak.wwise.core.object.nameChanged",
		                                            self._on_name_changed, return_options)
		
		self.notes_changed = _RefEvent(WwiseObjectInfo, str, str)
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_noteschanged.html
		\nSent when the object's notes are changed.
		\n**Event Data**:
		\n- A WwiseObjectInfo instance representing the object whose notes changed.
		\n- A string containing the old notes.
		\n- A string containing the new notes.
		"""
		
		self._notes_changed = self._client.subscribe("ak.wwise.core.object.notesChanged",
		                                             self._on_notes_changed, return_options)
		
		self.post_deleted = _RefEvent(WwiseObjectInfo)
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_postdeleted.html
		\nSent following an object's deletion.
		\n**Event Data**:
		\n- A WwiseObjectInfo instance representing the object that was deleted.
		"""
		
		self._post_deleted = self._client.subscribe("ak.wwise.core.object.postDeleted",
		                                            self._on_post_deleted, return_options)
		
		self.pre_deleted = _RefEvent(WwiseObjectInfo)
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_predeleted.html
		\nSent prior to an object's deletion.
		\n**Event Data**:
		\n- A WwiseObjectInfo instance representing the object that will be deleted.
		"""
		
		self._pre_deleted = self._client.subscribe("ak.wwise.core.object.preDeleted",
		                                           self._on_pre_deleted, return_options)
		
		self.property_changed = _RefEvent(WwiseObjectInfo, Name, _Any, _Any, GUID)
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_propertychanged.html
		\nSent when the watched property of an object changes.
		\n**Event Data**:
		\n- A WwiseObjectInfo instance representing the watched object.
		\n- The Name of the changed property.
		\n- The old value of the property. Can be of any type, but likely `None`, `str`, `float`, or `bool`.
		\n- The new value of the property. Can be of any type, but likely `None`, `str`, `float`, or `bool`.
		\n- The GUID of the platform for which the change occurred.
		\n**Additional Notes**:
		\n- This event requires a `watch_list` (a `tuple` of `WwiseObjectWatch`). See `pywwise.new_connection`.
		\n- This event will only happen for the objects and properties included in the `watch_list`.
		"""
		
		self._property_changed = list[_EventHandler]()
		for watch in watch_list:
			for prop in watch.properties:  # `property` is a built-in identifier, so using `prop` instead
				prop_options = dict(return_options)
				prop_options["object"] = watch.guid
				prop_options["property"] = prop
				self._property_changed.append(self._client.subscribe("ak.wwise.core.object.propertyChanged",
				                                                     self._on_property_changed, prop_options))
		
		self.reference_changed = _RefEvent(WwiseObjectInfo)
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_referencechanged.html
		\nSent when an object reference is changed.
		\n**Event Data**:
		\n- A WwiseObjectInfo instance representing the object that had a reference changed.
		\n- A WwiseObjectInfo instance representing the previous referenced object.
		\n- A WwiseObjectInfo instance representing the new referenced object.
		"""
		
		self._reference_changed = self._client.subscribe("ak.wwise.core.object.referenceChanged",
		                                                 self._on_reference_changed, return_options)
	
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
		info = WwiseObjectInfo.from_dict(kwargs["attenuation"])
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
		return WwiseObjectInfo.from_dict(kwargs["child"]), WwiseObjectInfo.from_dict(kwargs["parent"])
	
	@callback
	def _on_created(self, event, **kwargs):
		"""
		Callback function for the `created` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		obj = kwargs["object"]
		event(WwiseObjectInfo(GUID(obj["id"]),
		                      Name.get_null(),
		                      EObjectType.from_type_name(obj["type"]),
		                      ProjectPath.get_null()))
	
	@callback
	def _on_curve_changed(self, event, **kwargs):
		"""
		Callback function for the `curveChanged` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		event(WwiseObjectInfo.from_dict(kwargs["curve"]), WwiseObjectInfo.from_dict(kwargs["owner"]))
	
	@callback
	def _on_name_changed(self, event, **kwargs):
		"""
		Callback function for the `nameChanged` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		event(WwiseObjectInfo.from_dict(kwargs["object"]), kwargs["oldName"])
	
	@callback
	def _on_notes_changed(self, event, **kwargs):
		"""
		Callback function for the `notesChanged` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		event(WwiseObjectInfo.from_dict(kwargs["object"]), kwargs["newNotes"], kwargs["oldNotes"])
	
	@callback
	def _on_post_deleted(self, event, **kwargs):
		"""
		Callback function for the `postDeleted` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		event(WwiseObjectInfo.from_dict(kwargs["object"]))
	
	@callback
	def _on_pre_deleted(self, event, **kwargs):
		"""
		Callback function for the `preDeleted` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		event(WwiseObjectInfo.from_dict(kwargs["object"]))
	
	@callback
	def _on_property_changed(self, event, **kwargs):
		"""
		Callback function for the `propertyChanged` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		watch = WwiseObjectInfo.from_dict(kwargs["object"])  # this is the object where the change happened
		event(watch, Name(kwargs["property"]), kwargs["old"], kwargs["new"], GUID(kwargs["platform"]))
	
	@callback
	def _on_reference_changed(self, event, **kwargs):
		"""
		Callback function for the `referenceChanged` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		obj = WwiseObjectInfo.from_dict(kwargs["object"])
		old = WwiseObjectInfo.from_dict(kwargs["old"])
		new = WwiseObjectInfo.from_dict(kwargs["new"])
		event(obj, old, new)
	
	def copy(self, obj: GUID | tuple[EObjectType, Name] | ProjectPath,
	         parent: GUID | tuple[EObjectType, Name] | ProjectPath,
	         name_conflict_strategy: ENameConflictStrategy = ENameConflictStrategy.FAIL,
	         version_control_auto_checkout: bool = True,
	         version_control_auto_add: bool = True) -> WwiseObjectInfo | None:
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_copy.html \n
		Copies an object to the given parent. Note that if a Work Unit is copied, the operation cannot be undone and
		the project will be saved. This function calls `ak.wwise.core.object.get` to fetch the `path` and `type`
		attributes.
		:param obj: The GUID, type and name, or project path of the object to copy. Although using `Name` is supported,
					an object type (`EObjectType`) must be specified and only types with globally-unique names (e.g.
					`EObjectType.EVENT`) are supported.
		:param parent: The GUID, type and name, or project path of the new object's parent. Although using `Name` is
					   supported, an object type (`EObjectType`) must be specified and only types with globally-unique
					   names (e.g. `EObjectType.EVENT`) are supported.
		:param name_conflict_strategy: The strategy to use in case of a name conflict.
		:param version_control_auto_checkout: Determines if Wwise automatically performs a Checkout source control
											  operation for affected work units and for the project.
		:param version_control_auto_add: Determines if Wwise automatically performs an Add source control operation for
										 affected work units.
		:return: The new object as a WwiseObjectInfo, or None if the operation failed.
		"""
		args = {"object": f"{obj[0].get_type_name()}:{obj[1]}" if isinstance(obj, tuple) else obj,
		        "parent": f"{parent[0].get_type_name()}:{parent[1]}" if isinstance(parent, tuple) else parent,
		        "onNameConflict": name_conflict_strategy,
		        "autoCheckOutToSourceControl": version_control_auto_checkout,
		        "autoAddToSourceControl": version_control_auto_add}
		options = {"return": EReturnOptions.get_defaults()}
		
		results = self._client.call("ak.wwise.core.object.copy", args, options=options)
		if results is None:
			return None
		
		obj_info = self.get(f"$ from object \"{results.get("id", GUID.get_null())}\" take 1")  # force single match
		return obj_info[0] if len(obj_info) > 0 else None  # WwiseObjectInfo has valid path and type attributes
	
	def create(self, name: Name | str, etype: EObjectType, parent: GUID | tuple[EObjectType, Name] | ProjectPath,
	           name_conflict_strategy: ENameConflictStrategy = ENameConflictStrategy.FAIL, notes: str = "",
	           version_control_auto_checkout: bool = True, platform: Name | GUID = None) -> WwiseObjectInfo | None:
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_create.html \n
		Creates an object of type 'type', as a child of 'parent'. Refer to Importing Audio Files and Creating
		Structures for more information about creating objects. Also refer to `ak.wwise.core.audio.import_files` to
		import audio files to Wwise. To create Effect or Source plug-ins, use `ak.wwise.core.object.set`, and refer to
		Wwise Objects Reference for the classId.
		:param name: The name of the new Wwise object.
		:param etype: The type of the new Wwise object.
		:param parent: The GUID, typed name, or project path of the new object's parent.
		:param name_conflict_strategy: The strategy to adopt in case of name conflicts.
		:param notes: The notes to append to the new Wwise object.
		:param version_control_auto_checkout: Determines if Wwise automatically performs a Checkout source control
											  operation for affected work units and for the project.
		:param platform: Specify what platform to create the object for. Usually not necessary.
		:return: The new object as a WwiseObjectInfo, or None if the operation failed.
		"""
		args = dict()
		args["name"] = name
		args["type"] = etype.get_type_name()
		args["parent"] = f"{parent[0].get_type_name()}:{parent[1]}" if isinstance(parent, tuple) else parent
		args["onNameConflict"] = name_conflict_strategy.value
		args["notes"] = notes
		args["autoAddToSourceControl"] = version_control_auto_checkout
		if platform is not None:
			args["platform"] = platform
		
		results = self._client.call("ak.wwise.core.object.create", args)  # missing path, at this point
		if results is None:
			return None
		
		new_obj = self.get(f"$ from object \"{results.get("id", GUID.get_null())}\" take 1")
		return new_obj[0] if len(new_obj) > 0 else None
	
	def delete(self, obj: GUID | tuple[EObjectType, Name] | ProjectPath,
	           version_control_auto_checkout: bool = True) -> bool:
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_delete.html \n
		Deletes the specified object. Note that if a Work Unit is deleted, the operation cannot be undone
		and the project will be saved.
		:param obj: The GUID, typed name, or project path of the object to delete. Although using `Name` is supported,
					an object type (`EObjectType`) must be specified and only types with globally-unique names (e.g.
					`EObjectType.EVENT`) are supported.
		:param version_control_auto_checkout: Determines if Wwise automatically performs a Checkout source control
											  operation for affected work units and for the project.
		:return: Whether the operation succeeded.
		"""
		args = {"object": obj if not isinstance(obj, tuple) else f"{obj[0]}:{obj[1]}",
		        "autoCheckOutToSourceControl": version_control_auto_checkout}
		return self._client.call("ak.wwise.core.object.delete", args) is not None
	
	def diff(self, source: GUID | tuple[EObjectType, Name] | ProjectPath,
	         target: GUID | tuple[EObjectType, Name] | ProjectPath) -> tuple[tuple[str], tuple[str]]:
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_diff.html \n
		Compares properties and lists of the source object with those in the target object.
		:param source: The GUID, typed name, or project path of the "source" Wwise object.
		:param target: The GUID, typed name, or project path of the "target" Wwise object.
		:return: Two tuples: the first containing names of properties and references that differ, and the second
				 containing names of lists that differ.
		"""
		args = {"source": source if not isinstance(source, tuple) else f"{source[0]}:{source[1]}",
		        "target": target if not isinstance(target, tuple) else f"{target[0]}:{target[1]}"}
		results = self._client.call("ak.wwise.core.object.diff", args)
		return results.get("properties", tuple[str]()), results.get("lists", tuple[str]())
	
	def get(self, waql: WAQL | str, returns_and_properties: tuple[EReturnOptions | str, ...] = ()) -> tuple[
		WwiseObjectInfo, ...]:
		"""
		https://www.audiokinetic.comlibrary/edge/?source=SDK&id=ak_wwise_core_object_get.html \n
		Performs a query and returns the data, as specified in the options, for each object in the query result. The
		query should use the WAQL syntax.
		:param waql: A WAQL query, as either a WAQL object or a raw string. Note: **using the `select` statement for
					 objects is valid, but using it with properties (e.g. `Volume`) is invalid.**
		:param returns_and_properties: Additional return options (e.g. `EReturnOptions.WORK_UNIT`) and properties (e.g.
									   `"Volume"`, `"Pitch"`, etc.). Available properties depend on the type of object
									   found. For more information and a complete list of properties, check the **Wwise
									   Objects Reference** page on Audiokinetic's official documentation page. The
									   requested results will be available in the `other` property of each
									   `WwiseObjectInfo` instance.
		:return: A collection of `WwiseObjectInfo` instances representing the objects found.
		"""
		args = {"waql": str(waql)}  # str conversion needed because of JSON serialization
		
		options = {"return": [*EReturnOptions.get_defaults(), *returns_and_properties]}
		
		objects = self._client.call("ak.wwise.core.object.get", args, options=options)
		objects = objects.get("return", ()) if objects is not None else ()
		
		infos = list[WwiseObjectInfo]()
		for obj in objects:
			info = WwiseObjectInfo.from_dict(obj)
			info.other = {key: value for key, value in obj.items() if key not in EReturnOptions.get_defaults()}
			infos.append(info)
		
		return tuple(infos)
	
	def get_attenuation_curve(self, obj: GUID | Name | ProjectPath, etype: EAttenuationCurveType,
	                          platform: GUID | Name = None) -> AttenuationCurve | None:
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_getattenuationcurve.html \n
		Gets the specified attenuation curve for a given attenuation object.
		:param obj: The GUID,  name, or project path of the Attenuation object to get the curve from.
		:param etype: The type of the attenuation curve to get.
		:param platform: The GUID or unique name of the platform to get the curve from. If unspecified, the platform
						 used will be whichever one is active in the Wwise authoring app or console.
		:return:
		"""
		args = dict()
		args["object"] = obj if not isinstance(obj, Name) else f"{EObjectType.ATTENUATION}:{obj}"
		args["curveType"] = etype.value
		if platform is not None:
			args["platform"] = platform
		
		results = self._client.call("ak.wwise.core.object.getAttenuationCurve", args)
		if not results:  # invalid or empty
			return None
		
		points = tuple(GraphPoint2D(Vector2(point["x"], point["y"]),
		                            EnumStatics.from_value(EAttenuationCurveShape, point["shape"]))
		               for point in results["points"])
		usage = EnumStatics.from_value(EAttenuationCurveUsage, results["use"])
		etype = EnumStatics.from_value(EAttenuationCurveType, results["curveType"])
		
		return AttenuationCurve(points, usage, etype)
	
	def get_property_and_reference_names(self):
		"""
		Retrieves the list of property and reference names for an object.
		"""
	
	def get_property_info(self):
		"""
		Retrieves information about an object property. Note that this function does not return the value of a
		property. To retrieve the value of a property, refer to `ak.wwise.core.object.get` and Return Options.
		"""
	
	def get_types(self):
		"""
		Retrieves the list of all object types registered in Wwise's object model. This function returns the equivalent
		of Wwise Objects Reference.
		"""
	
	def is_linked(self):
		"""
		Indicates whether a property, reference, or object list is bound to a particular platform or to all platforms.
		"""
	
	def is_property_enabled(self):
		"""
		Returns true if a property is enabled based on the values of the properties it depends on.
		"""
	
	def move(self, obj: GUID | tuple[EObjectType, Name] | ProjectPath,
	         parent: GUID | tuple[EObjectType, Name] | ProjectPath,
	         name_conflict_strategy: ENameConflictStrategy = ENameConflictStrategy.FAIL,
	         version_control_auto_checkout: bool = True) -> WwiseObjectInfo | None:
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_move.html \n
		Moves an object to the given parent. Returns the moved object.
		:param obj: The GUID, typed name, or project path of the object to move. Although using `Name` is supported,
					an object type (`EObjectType`) must be specified and only types with globally-unique names (e.g.
					`EObjectType.EVENT`) are supported.
		:param parent: The GUID, typed name, or project path of the object's new parent. Although using `Name` is
					   supported, an object type (`EObjectType`) must be specified and only types with globally-unique
					   names (e.g. `EObjectType.EVENT`) are supported.
		:param name_conflict_strategy: The strategy to use in case of a name conflict.
		:param version_control_auto_checkout: Determines if Wwise automatically performs a Checkout source control
											  operation for affected work units and for the project.
		"""
		args = {"object": f"{obj[0].get_type_name()}:{obj[1]}" if isinstance(obj, tuple) else obj,
		        "parent": f"{parent[0].get_type_name()}:{parent[1]}" if isinstance(parent, tuple) else parent,
		        "onNameConflict": name_conflict_strategy,
		        "autoCheckOutToSourceControl": version_control_auto_checkout}
		
		results = self._client.call("ak.wwise.core.object.move", args)
		if results is None:
			return None
		
		obj_info = self.get(f"$ from object \"{results.get("id", GUID.get_null())}\" take 1")  # force single match
		return obj_info[0] if len(obj_info) > 0 else None  # WwiseObjectInfo has valid path and type attributes
	
	def paste_properties(self):
		"""
		Pastes properties, references and lists from one object to any number of target objects. Only those properties,
		references and lists which differ between source and target are pasted. Refer to Wwise Objects Reference for
		more information on the properties, references and lists available on each object type.
		"""
	
	def set(self):
		"""
		Allows for batch processing of the following operations: Object creation in a child hierarchy, Object creation
		in a list, Setting name, notes, properties and references. Refer to Importing Audio Files and Creating
		Structures for more information about creating objects. Also refer to `ak.wwise.core.audio.import_files` to
		import audio files to Wwise.
		"""
	
	def set_attenuation_curve(self):
		"""
		Sets the specified attenuation curve for a given attenuation object.
		"""
	
	def set_linked(self):
		"""
		Link or unlink a property/reference or object list to a particular platform.
		"""
	
	def set_name(self, obj: GUID | tuple[EObjectType, Name] | ProjectPath, new_name: Name | str) -> bool:
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_setname.html \n
		Renames an object.
		:param obj: The GUID, typed name, or project path of the object for which to set notes. Although using `Name`
					is supported, an object type (`EObjectType`) must be specified and only types with globally-unique
					names (e.g. `EObjectType.EVENT`) are supported.
		:param new_name: The new name.
		:return: Whether this call succeeded.
		"""
		args = {"object": obj if not isinstance(obj, tuple) else f"{obj[0]}:{obj[1]}", "value": new_name}
		return self._client.call("ak.wwise.core.object.setName", args) is not None
	
	def set_notes(self, obj: GUID | tuple[EObjectType, Name] | ProjectPath, notes: str) -> bool:
		"""
		https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_object_setnotes.html \n
		Sets the object's notes.
		:param obj: The GUID, typed name, or project path of the object for which to set notes. Although using `Name`
					is supported, an object type (`EObjectType`) must be specified and only types with globally-unique
					names (e.g. `EObjectType.EVENT`) are supported.
		:param notes: The new notes.
		:return: Whether this call succeeded.
		"""
		args = {"object": obj if not isinstance(obj, tuple) else f"{obj[0]}:{obj[1]}", "notes": notes}
		return self._client.call("ak.wwise.core.object.setNotes", args) is not None
	
	def set_property(self):
		"""
		Sets a property value of an object for a specific platform. Refer to Wwise Objects Reference for more
		information on the properties available on each object type. Refer to `ak.wwise.core.object.set_reference` to
		set a reference to an object. Refer to `ak.wwise.core.object.get` to obtain the value of a property for an
		object.
		"""
	
	def set_randomizer(self):
		"""
		Sets the randomizer values of a property of an object for a specific platform. Refer to Wwise Objects Reference
		for more information on the properties available on each object type.
		"""
	
	def set_reference(self):
		"""
		Sets an object's reference value. Refer to Wwise Objects Reference for more information on the references
		available on each object type.
		"""
	
	def set_state_groups(self):
		"""
		Sets the State Group objects associated with an object. Note, this will remove any previously associated State
		Group.
		"""
	
	def set_state_properties(self):
		"""
		Set the state properties of an object. Note, this will remove any previous state property, including the
		default ones.
		"""
