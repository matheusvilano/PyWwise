from datetime import datetime as _datetime
from os import makedirs as _makedirs
from base64 import b64decode as _b64decode
from typing import Any as _Any
from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient
from pywwise.ak.wwise.ui.commands import Commands as _Commands
from pywwise.ak.wwise.ui.project import Project as _Project
from pywwise.structs import Rect as _Rect, WwiseObjectInfo as _WwiseObjectInfo
from pywwise.enums import EReturnOptions as _EReturnOptions, EObjectType as _EObjectType
from pywwise.types import GUID as _GUID, Name as _Name, SystemPath as _SystemPath, ProjectPath as _ProjectPath
from pywwise.decorators import callback as _callback


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
		
		self.selection_changed = _RefEvent(tuple[_WwiseObjectInfo, ...])
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_selectionchanged.html
		\nSent when the selection changes in the project.
		\n**Event Data**:
		\n- A tuple of WwiseObjectInfo instances (each containing a GUID, a name, a type, and a path).
		"""
		
		selection_changed_options = {"return": [_EReturnOptions.GUID, _EReturnOptions.NAME,
		                                        _EReturnOptions.TYPE, _EReturnOptions.PATH]}
		self._selection_changed = self._client.subscribe("ak.wwise.ui.selectionChanged", self._on_selection_changed,
		                                                 selection_changed_options)
	
	@_callback
	def _on_selection_changed(self, **kwargs):
		"""
		Callback function for the `selectionChanged` event.
		:param kwargs: The event data.
		"""
		objects = list[_WwiseObjectInfo]()
		for obj in kwargs["objects"]:
			guid = _GUID(obj["id"])
			name = _Name(obj["name"])
			typename = _EObjectType.from_type_name(obj["type"])
			path = _ProjectPath(obj["path"])
			objects.append(_WwiseObjectInfo(guid, name, typename, path))
		self.selection_changed(tuple(objects))
	
	def bring_to_foreground(self) -> None:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_bringtoforeground.html \n
		Bring Wwise main window to foreground. Refer to `SetForegroundWindow` and `AllowSetForegroundWindow`
		on MSDN for more information on the restrictions. Refer to `ak.wwise.core.get_info` to obtain the
		Wwise process ID for `AllowSetForegroundWindow`.
		"""
		return self._client.call("ak.wwise.ui.bringToForeground")
	
	def capture_screen(self, view_name: str = None, view_selection_channel: int = None, capture_rect: _Rect = None,
	                   output_path: _SystemPath = None) -> tuple[str, str]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_capturescreen.html \n
		Captures a part of the Wwise UI relative to a view.
		:param view_name: The name of the view as displayed in Wwise UI. By default, the whole UI is captured.
		:param view_selection_channel: The selection channel of the view. Can be a value of 1, 2, 3 or 4. By default,
		the current selection channel of the view is detected automatically. If the specified value is out of bounds,
		the value will be clamped.
		:param capture_rect: The capture region. By default, the whole view is captured.
		:param output_path: If specified, a PNG image will be created at the specified location. If only directory
		names are specified (e.g. "C:/Users/PyWwise/Pictures"), the file name will be the current system date and time.
		:return: The underlying image data format and the encoded image data (Base64).
		"""
		args = {}
		
		if view_name is not None:
			args["viewName"] = view_name
		if view_selection_channel is not None:
			args["viewSelectionChannel"] = max(min(view_selection_channel, 4), 1)
		if capture_rect is not None:
			args["rect"] = {"x": capture_rect.x, "y": capture_rect.y, "width": capture_rect.width,
			                "height": capture_rect.height}
		
		results = self._client.call("ak.wwise.ui.captureScreen", args)
		content_type, content_base = results.get("contentType"), results.get("contentBase64")
		
		if output_path is not None:
			if output_path.suffix == "":
				date_time = _datetime.now()
				date = f"{date_time.year}-{date_time.month:02}-{date_time.day:02}"
				time = f"{date_time.hour:02}{date_time.minute:02}{date_time.second:02}"
				output_path /= f"Screenshot {date} {time}.png"
			if not output_path.exists():
				_makedirs(output_path.parent, exist_ok=True)
			with open(output_path, "wb") as image:
				image.write(_b64decode(content_base))
		
		return content_type, content_base
	
	def get_selected_objects(self, return_options: set[_EReturnOptions] = None, platform: str = None,
	                         language: str = None) -> tuple[_WwiseObjectInfo, ...]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_ui_getselectedobjects.html \n
		Retrieves the list of objects currently selected by the user in the active view.
		:param return_options: The additional return options. By default, this function returns only the GUID and Name
		of the selected objects.
		:param platform: If specified, this function will get information from the specified platform instead of the
		current platform.
		:param language: If specified, this function will get information from the specified language instead of the
		current language.
		:returns: For each selected object, a WwiseObjectInfo containing an object's GUID, name, path, type, and a
		dictionary containing additional information (requested via `return_options`). When accessing the values in the
		dictionary, use the EReturnOptions enum as the keys. If this function call fails, an empty tuple is returned.
		"""
		returns = (_EReturnOptions.GUID, _EReturnOptions.NAME, _EReturnOptions.TYPE, _EReturnOptions.PATH)
		options = {"return": set(returns)}  # to ensure only unique values
		
		if return_options is not None:
			options["return"].update(return_options)
		if platform is not None:
			options["platform"] = platform
		if language is not None:
			options["language"] = language
		
		options["return"] = [ret for ret in options["return"]]  # must be a list for JSON serialization
		
		results = self._client.call("ak.wwise.ui.getSelectedObjects", {}, options=options)
		results = results.get("objects") if results is not None else None
		if results is None:
			return ()
		
		objects = list[_WwiseObjectInfo]()
		
		for result in results:
			guid = _GUID(result[_EReturnOptions.GUID])
			name = _Name(result[_EReturnOptions.NAME])
			typename = _EObjectType.from_type_name(result[_EReturnOptions.TYPE])
			path = _ProjectPath(result[_EReturnOptions.PATH])
			other = {key: value for key, value in result.items() if key not in returns}
			objects.append(_WwiseObjectInfo(guid, name, typename, path, other))
		
		return tuple(objects)
