from waapi import WaapiClient as _WaapiClient


class Log:
    """ak.wwise.core.log"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def add_tem(self):
        """
        Adds a new item to the logs on the specified channel.
        """

    def clear(self):
        """
        Clears the logs on the specified channel.
        """

    def get(self):
        """
        Retrieves the latest log for a specific channel. Refer to `ak.wwise.core.log.item_added` to be
        notified when an item is added to the log. The log is empty when used in WwiseConsole.
        """
