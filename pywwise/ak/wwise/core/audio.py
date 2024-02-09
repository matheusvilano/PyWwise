from waapi import WaapiClient as _WaapiClient


class Audio:
    """ak.wwise.core.audio"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def import_files(self):
        """
        Creates Wwise objects and imports audio files. This function does not return an error when
        something fails during the import process, please refer to the log for the result of each import
        command. This function uses the same importation processor available through the Tab Delimited
        import in the Audio File Importer. The function returns an array of all objects created,
        replaced or re-used. Use the options to specify how the objects are returned. For more
        information, refer to Importing Audio Files and Creating Structures.
        """
        # "import" is a reserved keyword, so function name does not match WAAPI

    def import_tab_delimited(self):
        """
        Scripted object creation and audio file import from a tab-delimited file.
        """

    def mute(self):
        """
        Mutes an object.
        """

    def reset_mute(self):
        """
        Unmute all muted objects.
        """

    def reset_solo(self):
        """
        Unsolo all soloed objects.
        """

    def solo(self):
        """
        Solos an object.
        """
