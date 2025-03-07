# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pywwise.objects.types.rtpc import Rtpc

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour, EEnvelopeTriggerOn, EModulatorScopeLimited
from pywwise.objects.abc import WwiseObject


class ModulatorTime(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_modulatortime.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MODULATOR_TIME`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    envelope_stop_playback = WwiseProperty[bool]("EnvelopeStopPlayback", bool)
    envelope_trigger_on = WwiseProperty[EEnvelopeTriggerOn]("EnvelopeTriggerOn", EEnvelopeTriggerOn)
    modulator_scope = WwiseProperty[EModulatorScopeLimited]("ModulatorScope", EModulatorScopeLimited)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    rtpc: WwiseProperty[tuple[Rtpc, ...]] = WwiseProperty("RTPC", tuple)  # Using `:` to avoid circular imports.
    time_mod_duration = WwiseProperty[float]("TimeModDuration", float)
    time_mod_initial_delay = WwiseProperty[float]("TimeModInitialDelay", float)
    time_mod_loops = WwiseProperty[int]("TimeModLoops", int)
    time_mod_playback_rate = WwiseProperty[float]("TimeModPlaybackRate", float)
