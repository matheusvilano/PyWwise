from waapi import WaapiClient as _WaapiClient


class Undo:
    """ak.wwise.core.undo"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def begin_group(self):
        """
        Begins an undo group. Make sure to call ak.wwise.core.undo.endGroup exactly once for every
        ak.wwise.core.beginUndoGroup call you make. Calls to `ak.wwise.core.undo.begin_group` can be nested.
        When closing a WAMP session, a check is made to ensure that all undo groups are closed. If not,
        a cancelGroup is called for each of the groups still open.
        """

    def cancel_group(self):
        """
        Cancels the last undo group.
        """

    def end_group(self):
        """
        Ends the last undo group.
        """

    def redo(self):
        """
        Redoes the last operation in the Undo stack.
        """

    def undo(self):
        """
        Undoes the last operation in the Undo stack.
        """
