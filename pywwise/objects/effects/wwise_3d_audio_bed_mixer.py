# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EAudioObjectOptions, EMainMixConfiguration, EPassthroughMixPolicy
from pywwise.objects.abc import WwiseObject


class Wwise3DAudioBedMixer(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_3d_audio_bed_mixer.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_3D_AUDIO_BED_MIXER`.
    """
    main_mix_configuration = WwiseProperty[EMainMixConfiguration]("MainMixConfiguration", EMainMixConfiguration)
    passthrough_mix_policy = WwiseProperty[EPassthroughMixPolicy]("PassThroughMixPolicy", EPassthroughMixPolicy)
    system_audio_object_limit = WwiseProperty[int]("SystemAudioObjectLimit", int)
    system_audio_objects_policy = WwiseProperty[EAudioObjectOptions]("SystemAudioObjectsPolicy", EAudioObjectOptions)
