# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient


class Waapi:
    """ak.wwise.ui.waapi"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
    
    def get_functions(self) -> tuple[str, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_waapi_getfunctions.html \n
        Retrieves the list of functions.
        :return: A tuple containing the URI of all WAAPI functions.
        """
        results = self._client.call("ak.wwise.waapi.getFunctions")
        return tuple(results.get("functions")) if results is not None else ()
    
    def get_schema(self, uri: str) -> dict | None:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_waapi_getschema.html \n
        Retrieves the JSON schema of a Waapi URI.
        :param uri: The URI to get the schema for (e.g. "ak.wwise.waapi.getSchema" gets the schema for this function).
        :return: If the call succeeded, a JSON-like dictionary representing the schema of the specified URI; else, None.
        """
        return self._client.call("ak.wwise.waapi.getSchema", {"uri": uri})
    
    def get_topics(self) -> tuple[str, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_waapi_gettopics.html \n
        Retrieves the list of topics to which a client can subscribe.
        :return: A tuple containing the URI of all WAAPI topics.
        """
        results = self._client.call("ak.wwise.waapi.getTopics")
        return tuple(results.get("topics")) if results is not None else ()
