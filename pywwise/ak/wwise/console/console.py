from waapi import WaapiClient as _WaapiClient
from pywwise.ak.wwise.console.project import Project as _Project


class Console:
    """ak.wwise.console"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
        self.project = _Project(self._client)
