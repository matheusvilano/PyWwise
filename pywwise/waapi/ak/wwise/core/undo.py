# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient


class Undo:
    """ak.wwise.core.undo"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
    
    def begin_group(self) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_undo_begingroup.html \n
        Begins an undo group. Make sure to call ak.wwise.core.undo.endGroup exactly once for every
        ak.wwise.core.beginUndoGroup call you make. Calls to `ak.wwise.core.undo.begin_group` can be nested.
        When closing a WAMP session, a check is made to ensure that all undo groups are closed. If not,
        a cancelGroup is called for each of the groups still open.
        :return: Whether the call was successful.
        """
        return self._client.call("ak.wwise.core.undo.beginGroup") is not None
    
    def cancel_group(self, undo: bool = False) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_undo_cancelgroup.html \n
        Cancels the last undo group.
        :param undo: Specify if the operations are undone.
        :return: Whether the call was successful.
        """
        return self._client.call("ak.wwise.core.undo.cancelGroup", {"undo": undo}) is not None
    
    def end_group(self, display_name: str) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_undo_endgroup.html \n
        Ends the last undo group.
        :param display_name: The name that is displayed in the history for this undo group.
        :return: Whether the call was successful.
        """
        return self._client.call("ak.wwise.core.undo.endGroup", {"displayName": display_name}) is not None
    
    def redo(self) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_undo_redo.html \n
        Redoes the last operation in the Undo stack.
        :return: Whether the call was successful.
        """
        return self._client.call("ak.wwise.core.undo.redo") is not None
    
    def undo(self) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_undo_undo.html \n
        Undoes the last operation in the Undo stack.
        :return: Whether the call was successful.
        """
        return self._client.call("ak.wwise.core.undo.undo") is not None
