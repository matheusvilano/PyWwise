# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import ERecorderAmbisonicsChannelOrdering, ERecorderFormat
from pywwise.objects.abc import WwiseObject


class WwiseRecorder(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_recorder.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_RECORDER`.
    """
    ambisonics_channel_ordering = WwiseProperty[ERecorderAmbisonicsChannelOrdering](
        "AmbisonicsChannelOrdering", ERecorderAmbisonicsChannelOrdering)
    apply_downstream_volume = WwiseProperty[bool]("ApplyDownstreamVolume", bool)
    authoring_filename = WwiseProperty[str]("AuthoringFilename", str)
    centre = WwiseProperty[float]("Center", float)
    downmix_to_stereo = WwiseProperty[bool]("DownmixToStereo", bool)
    format = WwiseProperty[ERecorderFormat]("Format", ERecorderFormat)
    game_filename = WwiseProperty[str]("GameFilename", str)
    lfe = WwiseProperty[float]("LFE", float)
    rear = WwiseProperty[float]("Rear", float)
    surround = WwiseProperty[float]("Surround", float)
