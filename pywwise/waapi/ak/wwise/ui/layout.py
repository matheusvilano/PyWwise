# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0
from typing import Tuple

from waapi import WaapiClient as _WaapiClient

from pywwise.primitives import GameObjectID, GUID, Name
from pywwise.structs import LayoutRectangle, ViewInstance, ViewType
from pywwise.enums import EDockViewSides

class Layout:
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
    
    def dock_view(self, layout_name: Name, view_id: GUID, target_id: GUID, dock_side: EDockViewSides) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_dockview.html \n
        Dock a floating view into a layout.
        :param layout_name: The name of the layout where the view will be docked.
        :param view_id: The unique ID (GUID) of the view to dock.
        :param target_id: The unique ID (GUID) of the target element.
        :param dock_side: The side where to drop the view on the target. These sides are defined as enum values via the
                          EDockViewSides enum.
        :return: True if the call was successful, False otherwise.
        """
        args = {"name": layout_name, "viewID": view_id, "targetID": target_id, "side": dock_side}
        
        return self._client.call("ak.wwise.ui.layout.dockView", args) is not None
    
    def get_current_layout_name(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getcurrentlayoutname.html \n
        Retrieves the current layout name.
        :return: The Name of the current layout. If no layout is currently active, an empty Name is returned.
        """
        results = self._client.call("ak.wwise.ui.layout.getCurrentLayoutName", dict())
        
        if results is None:
            return Name.get_null()
        
        return results.get("name", "")
    
    def get_element_rectangle(self, element_id: GameObjectID) -> LayoutRectangle:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getelementrectangle.html \n
        Retrieves the current allocated rectangle of a layout element. An empty rect is returned if the element is not found.
        :return: A LayoutRectangle object. Will be empty if the element is not found.
        """
        args = {"id": element_id}
        
        result = self._client.call("ak.wwise.ui.layout.getElementRectangle", args)
        
        if result is None:
            return LayoutRectangle.get_zero()
        
        return LayoutRectangle(result.get("x", 0),
                               result.get("top", 0),
                               result.get("right", 0),
                               result.get("bottom", 0))
    
    def get_layout(self, layout_name: Name):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getlayout.html\n
        Serializes a specific layout into a JSON format.
        :return: A layout object in JSON format.
        """
        pass
    
    def get_layout_names(self) -> Tuple[Name, ...]:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getlayoutnames.html \n
        Retrieves a list of the factory layout names.
        :returns: A tuple of all factory layout names.
        """
        results = self._client.call("ak.wwise.ui.layout.getLayoutNames", dict())
        
        if not results or "layouts" not in results:
            return Tuple[Name, ...]()
        
        layout_names = list[Name]()
        
        for layout in results["layouts"]:
            layout_names.append(layout)
        
        return Tuple[Name, ...](layout_names)
    
    def get_or_create_view(self, name: Name, pos_x: int = -1, pos_y: int = -1) -> GUID:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getorcreateview.html \n
        Gets a view, if it exists in the current layout, or creates a new one.
        :param name: The name of the layout from which to undock the view.
        :param pos_x: Position of the undocked view on the horizontal axis. Defaults to -1.
        :param pos_y: Position of the undocked view on the vertical axis. Defaults to -1.
        :return: The unique GUID of the view
        """
        args = {"name": name, "posX": pos_x, "posY": pos_y}
        
        results = self._client.call("ak.wwise.ui.layout.getOrCreateView", args)
        
        if results is None:
            return GUID.get_null()
        
        return results.get("id")
    
    def get_view_instances(self, layout_name: Name) -> Tuple[ViewInstance, ...]:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getviewinstances.html \n
        Retrieves a list of all view instances of a layout.
        :param layout_name: The name of the layout to inspect.
        :returns: A tuple of all View Instances of a Layout.
        """
        args = {"name": layout_name}
        
        results = self._client.call("ak.wwise.ui.layout.getViewInstances", args)
        
        if not results or "viewInstances" not in results:
            return Tuple[ViewInstance, ...]()
        
        view_instance_objects = list[ViewInstance]()
        
        for view_instance_object in results["viewInstances"]:
            view_instance_objects.append(ViewInstance(view_name=view_instance_object.get("name", ""),
                                                      view_id=view_instance_object.get("viewID", ""),
                                                      view_is_docked=view_instance_object.get("viewIsDocked", False),
                                                      view_display_name=view_instance_object.get("viewDisplayName", "")
                                                      ))
        
        return Tuple[ViewInstance, ...](view_instance_objects)
    
    def get_view_types(self) -> Tuple[ViewType, ...]:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getviewtypes.html \n
        Retrieves a list of all view types registered in Wwise.
        :returns: A tuple of all View Types registered in Wwise.
        """
        results = self._client.call("ak.wwise.ui.layout.getViewTypes", dict())
        
        if not results or "viewTypes" not in results:
            return Tuple[ViewType, ...]()
        
        view_type_objects = list[ViewType]()
        
        for view_type_object in results["viewTypes"]:
            view_type_objects.append(ViewType(view_name=view_type_object.get("viewName", ""),
                                              view_display_name=view_type_object.get("viewDisplayName", "")))
        
        return Tuple[ViewType, ...](view_type_objects)
    
    def move_splitter(self, splitter_id: GameObjectID, delta: int):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_movesplitter.html \n
        Moves a splitter by a delta given in pixels.
        :param splitter_id: The ID of the splitter to move.
        :param delta: The delta, in pixels, to add to the splitter position.
        :return: True if the call was successful, False otherwise.
        """
        args = {"id": splitter_id, "delta": delta}
        
        return self._client.call("ak.wwise.ui.layout.moveSplitter", args) is not None
    
    def remove_layout(self, layout_name: Name) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_removelayout.html \n
        Unregisters a temporary layout, previously registered with ak.wwise.ui.layout.setLayout.
        :return: True if the call was successful, False otherwise.
        """
        args = {"name": layout_name}
        
        return self._client.call("ak.wwise.ui.layout.removeLayout", args) is not None
    
    def set_layout(self, layout_name: Name):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_setlayout.html \n
        Registers a new layout from a JSON format.
        :param layout_name: The name of the layout to register.
        :return: None.
        """
        pass
    
    def switch_layout(self, layout_name: Name) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_switchlayout.html \n
        Switches the current layout.
        :param layout_name: The name of the layout to load.
        :return: True if the call was successful, False otherwise.
        """
        args = {"name": layout_name}
        
        return self._client.call("ak.wwise.ui.layout.switchLayout", args) is not None
    
    def undock_view(self, name: Name, view_id: GUID, pos_x: int = 0, pos_y: int = 0) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_undockview.html \n
        Undock a view from a layout.
        :param name: The name of the layout from which to undock the view.
        :param view_id: The unique id (GUID) of the view to undock.
        :param pos_x: Position of the undocked view on the horizontal axis. Defaults to 0.
        :param pos_y: Position of the undocked view on the vertical axis. Defaults to 0.
        :return: True if the call was successful, False otherwise.
        """
        args = {"name": name, "viewID": view_id, "posX": pos_x, "posY": pos_y}
        
        return self._client.call("ak.wwise.ui.layout.undockView", args) is not None
