from waapi import WaapiClient as _WaapiClient


class Waapi:
    """ak.wwise.ui.waapi"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def get_functions(self):
        """
        Retrieves the list of functions.
        """

    def get_schema(self):
        """
        Retrieves the JSON schema of a Waapi URI.
        """

    def get_topics(self):
        """
        Retrieves the list of topics to which a client can subscribe.
        """
