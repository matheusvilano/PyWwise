# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EBuiltInGameParameter, EColour, EInterpolationMode
from pywwise.objects.abc import WwiseObject


class GameParameter(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_gameparameter.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.GAME_PARAMETER`.
    """
    bind_to_built_in_param = WwiseProperty[EBuiltInGameParameter]("BindToBuiltInParam", EBuiltInGameParameter)
    colour = WwiseProperty[EColour]("Color", EColour)
    filter_time_down = WwiseProperty[float]("FilterTimeDown", float)
    filter_time_up = WwiseProperty[float]("FilterTimeUp", float)
    initial_value = WwiseProperty[float]("InitialValue", float)
    max = WwiseProperty[float]("Max", float)
    min = WwiseProperty[float]("Min", float)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    rtpc_ramping = WwiseProperty[EInterpolationMode]("RTPCRamping", EInterpolationMode)
    simulation_value = WwiseProperty[float]("SimulationValue", float)
    slew_rate_down = WwiseProperty[float]("SlewRateDown", float)
    slew_rate_up = WwiseProperty[float]("SlewRateUp", float)
