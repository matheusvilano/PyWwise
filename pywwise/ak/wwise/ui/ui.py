from waapi import WaapiClient as _WaapiClient
from pywwise.ak.wwise.ui.commands import Commands as _Commands
from pywwise.ak.wwise.ui.project import Project as _Project
from pywwise.structs import CaptureRect as _CaptureRect
from pywwise.enums import EReturnOptions as _ReturnOptions


class UI:
	"""ak.wwise.ui"""
	
	def __init__(self, client: _WaapiClient):
		"""
        Constructor.
        :param client: The WAAPI client to use.
        """
		self._client = client
		self.commands = _Commands(client)
		self.project = _Project(client)
	
	def bring_to_foreground(self):
		"""
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_bringtoforeground.html \n
        Bring Wwise main window to foreground. Refer to `SetForegroundWindow` and `AllowSetForegroundWindow`
        on MSDN for more information on the restrictions. Refer to `ak.wwise.core.get_info` to obtain the
        Wwise process ID for `AllowSetForegroundWindow`.
        """
		return self._client.call("ak.wwise.ui.bringToForeground")
	
	def capture_screen(self, view_name: str, view_selection_channel: int, capture_rect: _CaptureRect) -> tuple[
		str, str]:
		"""
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_capturescreen.html \n
        Captures a part of the Wwise UI relative to a view.
        :param view_name: The name of the view as displayed in Wwise UI. By default, the whole UI is captured.
        :param view_selection_channel: The selection channel of the view. Can be a value of 1, 2, 3 or 4. By default,
        the current selection channel of the view is detected automatically.
        :param capture_rect: The capture region. By default, the whole view is captured.
        :return: The underlying image data format and The encoded image data.
        """
		if not (1 <= view_selection_channel <= 4):
			print("Error. View Selection Channel out of bounds. Using default value of 1")
		view_selection_channel = 1
		
		args = {"viewName": view_name, "viewSelectionChannel": view_selection_channel,
		        "rect": {"x": capture_rect.x, "y": capture_rect.y, "width": capture_rect.width,
		                 "height": capture_rect.height}}
		results = self._client.call("ak.wwise.ui.captureScreen", args)
		return results.get("contentType"), results.get("contentBase64")
	
	def get_selected_objects(self, return_options: set[_ReturnOptions] = None, platform: str = None,
	                         language: str = None) -> list[dict]:
		"""
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_getselectedobjects.html \n
        Retrieves the list of objects currently selected by the user in the active view.
        """
		options = dict()
		if return_options is not None:
			options["return"] = list(return_options)
		if platform is not None:
			options["platform"] = platform
		if language is not None:
			options["language"] = language
		
		results = self._client.call("ak.wwise.ui.getSelectedObjects", options=options)
		return results.get("objects", [])