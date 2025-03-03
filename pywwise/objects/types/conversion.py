# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EChannelConversionSettings, EColour, ESampleRate, ESampleRateConversionQuality
from pywwise.objects.abc import WwiseObject


class Conversion(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_conversion.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.CONVERSION`.
    """
    allow_channel_upmix = WwiseProperty[bool]("AllowChannelUpmix", bool)
    channels = WwiseProperty[EChannelConversionSettings]("Channels", EChannelConversionSettings)
    colour = WwiseProperty[EColour]("Color", EColour)
    lr_mix = WwiseProperty[float]("LRMix", float)
    max_sample_rate = WwiseProperty[ESampleRate]("MaxSampleRate", ESampleRate)
    min_sample_rate = WwiseProperty[ESampleRate]("MinSampleRate", ESampleRate)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    remove_dc_offset = WwiseProperty[bool]("RemoveDCOffset", bool)
    sr_conversion_quality = WwiseProperty[ESampleRateConversionQuality](
        "SRConversionQuality", ESampleRateConversionQuality)
    sample_rate = WwiseProperty[ESampleRate]("SampleRate", ESampleRate)
    use_dither = WwiseProperty[bool]("UseDither", bool)
    use_filename_marker = WwiseProperty[bool]("UseFilenameMarker", bool)
