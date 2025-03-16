# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient


class Layout:
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
    
    def dock_view(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_dockview.html \n
        Dock a floating view into a layout.
        :return:
        """
        pass
    
    def get_current_layout_name(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getcurrentlayoutname.html \n
        Retrieves the current layout name.
        :return:
        """
        pass
    
    def get_element_rectangle(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getelementrectangle.html \n
        Retrieves the current allocated rectangle of a layout element. An empty rect is returned if the element is not found.
        :return:
        """
        pass
    
    def get_layout(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getlayout.html\n
        Serializes a specific layout into a JSON format.
        :return:
        """
        pass
    
    def get_layout_names(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getlayoutnames.html \n
        Retrieves a list of the factory layout names.
        :return:
        """
        pass
    
    def get_or_create_view(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getorcreateview.html \n
        Gets a view, if it exists in the current layout, or creates a new one.
        :return:
        """
        pass
    
    def get_view_instances(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getviewinstances.html \n
        Retrieves a list of all view instances of a layout.
        :return:
        """
        pass
    
    def get_view_types(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_getviewtypes.html \n
        Retrieves a list of all view types registered in Wwise.
        :return:
        """
        pass
    
    def move_splitter(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_movesplitter.html \n
        Moves a splitter by a delta given in pixels.
        :return:
        """
        pass
    
    def remove_layout(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_removelayout.html \n
        Unregisters a temporary layout, previously registered with ak.wwise.ui.layout.setLayout.
        :return:
        """
        pass
    
    def set_layout(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_setlayout.html \n
        Registers a new layout from a JSON format.
        :return:
        """
        pass
    
    def switch_layout(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_switchlayout.html \n
        Switches the current layout.
        :return:
        """
        pass
    
    def undock_view(self):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_layout_undockview.html \n
        Undock a view from a layout.
        :return:
        """
        pass
