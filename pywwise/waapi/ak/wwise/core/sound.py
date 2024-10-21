# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient

from pywwise.enums import EObjectType
from pywwise.primitives import GUID, Name, ProjectPath
from pywwise.structs import PlatformInfo


class Sound:
    """ak.wwise.core.sound"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
    
    def set_active_source(self, sound: GUID | Name | ProjectPath, source: GUID | Name | ProjectPath,
                          platform: PlatformInfo | Name | GUID = None) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_sound_setactivesource.html \n
        Sets which version of the source is being used for the specified sound. Use `ak.wwise.core.object.get` with the
        'activeSource' return option to get the active source of a sound.
        :param sound: The GUID or the project path of the sound for which to set the active source.
        :param source: The GUID or the project path of the source.
        :param platform: The platform on which to execute this operation. By default, the active platform in the Wwise
                         instance will be used.
        :return: Whether the call succeeded.
        """
        args = {"sound": f"{EObjectType.SOUND}{sound}" if isinstance(sound, Name) else sound,
                "source": f"{EObjectType.AUDIO_SOURCE}{source}" if isinstance(source, Name) else source}
        if platform is not None:
            args["platform"] = platform
        return self._client.call("ak.wwise.core.sound.setActiveSource", args) is not None
