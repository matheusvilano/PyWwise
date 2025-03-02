# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour
from pywwise.objects.abc import WwiseObject


class AcousticTexture(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_acoustictexture.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.ACOUSTIC_TEXTURE`.
    """
    absorption_high = WwiseProperty[float]("AbsorptionHigh", float)
    absorption_low = WwiseProperty[float]("AbsorptionLow", float)
    absorption_mid_high = WwiseProperty[float]("AbsorptionMidHigh", float)
    absorption_mid_low = WwiseProperty[float]("AbsorptionMidLow", float)
    absorption_offset = WwiseProperty[float]("AbsorptionOffset", float)
    colour = WwiseProperty[EColour]("Color", EColour)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    scattering = WwiseProperty[float]("Scattering", float)
