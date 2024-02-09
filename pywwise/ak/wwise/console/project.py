from waapi import WaapiClient as _WaapiClient


class Project:
    """ak.wwise.console.project"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def close(self):
        """
        Closes the current project. This operation is synchronous.
        """

    def create(self):
        """
        Creates, saves and opens new empty project, specified by path and platform. The project has no
        factory setting WorkUnit. This operation is synchronous.
        """

    def open(self):
        """
        Opens a project, specified by path. This operation is synchronous.
        """
