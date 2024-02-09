from waapi import WaapiClient as _WaapiClient


class Project:
    """ak.wwise.ui.project"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def close(self):
        """
        Closes the current project.
        """

    def create(self):
        """
        Creates, saves and opens new empty project, specified by path and platform. The project has no
        factory setting WorkUnit. Please refer to `ak.wwise.core.project.loaded` for further explanations
        on how to be notified when the operation has completed.
        """

    def open(self):
        """
        Opens a project, specified by path. Please refer to `ak.wwise.core.project.loaded` for further
        explanations on how to be notified when the operation has completed.
        """
