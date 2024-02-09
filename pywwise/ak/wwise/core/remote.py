from waapi import WaapiClient as _WaapiClient


class Remote:
    """ak.wwise.core.remote"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def connect(self):
        """
        Connects the Wwise Authoring application to a Wwise Sound Engine running executable or to a saved
        profile file. The host must be running code with communication enabled. If only "host" is
        provided, Wwise connects to the first Sound Engine instance found. To distinguish between
        different instances, you can also provide the name of the application to connect to.
        """

    def disconnect(self):
        """
        Disconnects the Wwise Authoring application from a connected Wwise Sound Engine running executable.
        """

    def get_available_consoles(self):
        """
        Retrieves all consoles available for connecting Wwise Authoring to a Sound Engine instance.
        """

    def get_connection_status(self):
        """
        Retrieves the connection status.
        """
