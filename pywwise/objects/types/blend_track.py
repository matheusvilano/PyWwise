# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.rtpc import Rtpc


class BlendTrack(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_blendtrack.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.BLEND_TRACK`.
    """
    enable_cross_fading = WwiseProperty[bool]("EnableCrossFading", bool)
    highpass = WwiseProperty[int]("Highpass", int)
    layer_cross_fade_control_input = WwiseProperty[Rtpc]("LayerCrossFadeControlInput", Rtpc)
    lowpass = WwiseProperty[int]("Lowpass", int)
    make_up_gain = WwiseProperty[float]("MakeUpGain", float)
    pitch = WwiseProperty[int]("Pitch", int)
    rtpc = WwiseProperty[tuple[Rtpc, ...]]("RTPC", tuple)
    volume = WwiseProperty[float]("Volume", float)
