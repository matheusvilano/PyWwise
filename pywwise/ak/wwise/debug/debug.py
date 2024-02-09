from waapi import WaapiClient as _WaapiClient


class Debug:
    """ak.wwise.debug"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def enable_asserts(self):
        """
        Enables debug assertions. Every call to enableAsserts with 'false' increments the ref count. Calling
        with true decrements the ref count. This is only available with Debug builds.
        """

    def enable_automation_mode(self):
        """
        Enables or disables the automation mode for Wwise. This reduces the potential interruptions caused by
        message boxes and dialogs. For instance, enabling the automation mode silently accepts: project
        migration, project load log, EULA acceptance, project licence display and generic message boxes.
        """

    def generate_tone_wav(self):
        """
        Generate a WAV file playing a tone with a simple envelope and save it to the specified location. This
        is provided as a utility to generate test WAV files.
        """

    def get_wal_tree(self):
        """
        Retrieves the WAL tree, which describes the nodes that are synchronized in the Sound Engine. Private
        use only.
        """

    def restart_waapi_servers(self):
        """
        Restart WAAPI servers. For internal use only.
        """

    def test_assert(self):
        """
        Private use only.
        """

    def test_crash(self):
        """
        Private use only.
        """
