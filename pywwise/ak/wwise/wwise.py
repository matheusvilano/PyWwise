from waapi import WaapiClient as _WaapiClient
from pywwise.ak.wwise.console import Console as _Console
from pywwise.ak.wwise.debug import Debug as _Debug
from pywwise.ak.wwise.core import Core as _Core
from pywwise.ak.wwise.ui import UI as _UI


class Wwise:
    """ak.wwise"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
        self.console = _Console(client)
        self.core = _Core(client)
        self.debug = _Debug(client)
        self.ui = _UI(client)