# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient

from pywwise.enums import EGameParameterValueChangeAction
from pywwise.primitives import GUID, Name, ProjectPath


class GameParameter:
    """ak.wwise.core.GameParameter"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
    
    def set_range(self, game_parameter: GUID | Name | ProjectPath, min_value: float, max_value: float,
                  on_curve_update: EGameParameterValueChangeAction) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_gameparameter_setrange.html \n
        Sets the Min and Max properties on a Game Parameter. Modifies the RTPC curves and blend tracks that use this
        Game Parameter for their X axis.
        :param game_parameter: The GUID, Name, or the project path of the Game Parameter.
        :param min_value: The minimum value of the Game Parameter.
        :param max_value: The maximum value of the Game Parameter.
        :param on_curve_update: Modifying the Min or Max value of a Game Parameter affects the RTPC curves and blend
                                tracks that use that Game Parameter for their X axis. Two actions are possible, Stretch
                                or PreserveX.
        :return: True if the call was successful, False otherwise.
        """
        args = {"object": game_parameter, "min": min_value, "max": max_value,
                "onCurveUpdate": on_curve_update}
        
        return self._client.call("ak.wwise.core.gameParameter.setRange", args) is not None
