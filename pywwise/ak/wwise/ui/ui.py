from waapi import WaapiClient as _WaapiClient
from pywwise.ak.wwise.ui.commands import Commands as _Commands
from pywwise.ak.wwise.ui.project import Project as _Project


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
        Bring Wwise main window to foreground. Refer to `SetForegroundWindow` and `AllowSetForegroundWindow`
        on MSDN for more information on the restrictions. Refer to `ak.wwise.core.get_info` to obtain the
        Wwise process ID for `AllowSetForegroundWindow`.
        """

    def capture_screen(self):
        """
        Captures a part of the Wwise UI relative to a view.
        """

    def get_selected_objects(self):
        """
        Retrieves the list of objects currently selected by the user in the active view.
        """
