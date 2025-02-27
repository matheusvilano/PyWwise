# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.objects.types import WwiseObject
from pywwise.descriptors import WwiseProperty


class Conversion(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_conversion.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.CONVERSION`.
    """
    allow_channel_upmix = WwiseProperty[bool]("AllowChannelUpmix", bool)
    channels = WwiseProperty[int]("Channels", int)
    colour = WwiseProperty[int]("Color", int)
    lr_mix = WwiseProperty[float]("LRMix", float)
    max_sample_rate = WwiseProperty[int]("MaxSampleRate", int)
    min_sample_rate = WwiseProperty[int]("MinSampleRate", int)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    remove_dc_offset = WwiseProperty[bool]("RemoveDCOffset", bool)
    sr_conversion_quality = WwiseProperty[int]("SRConversionQuality", int)
    sample_rate = WwiseProperty[int]("SampleRate", int)
    use_dither = WwiseProperty[bool]("UseDither", bool)
    use_filename_marker = WwiseProperty[bool]("UseFilenameMarker", bool)
