from waapi import WaapiClient as _WaapiClient


class Commands:
    """ak.wwise.ui.commands"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def execute(self):
        """
        Executes a command. Some commands can take a list of objects as parameters. Refer to Wwise
        Authoring Command Identifiers for the available commands.
        """

    def get_commands(self):
        """
        Gets the list of commands.
        """

    def register(self):
        """
        Registers an array of add-on commands. Registered commands remain until the Wwise process is
        terminated. Refer to Defining Command Add-ons for more information about registering commands.
        Also refer to `ak.wwise.ui.commands.executed`.
        """

    def unregister(self):
        """
        Unregisters an array of add-on UI commands.
        """
