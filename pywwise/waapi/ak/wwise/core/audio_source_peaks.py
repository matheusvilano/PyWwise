# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from waapi import WaapiClient as _WaapiClient

from pywwise.enums import EObjectType
from pywwise.primitives import GUID, Name, ProjectPath


class AudioSourcePeaks:
    """ak.wwise.core.audioSourcePeaks"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
    
    def get_min_max_peaks_in_region(self, source: GUID | Name | ProjectPath, time_from: float, time_to: float,
                                    num_peaks: int, cross_channel_peaks: bool = False) -> tuple[
        tuple[bytes, ...], int, float, float, float, str]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_audiosourcepeaks_getminmaxpeaksinregion.html \n
        Gets the min/max peak pairs, in the given region of an audio source, as a collection of binary strings (one per
        channel). The strings are base-64 encoded, 16-bit signed int arrays, with min and max values being interleaved.
        If getCrossChannelPeaks is true, only one binary string represents the peaks across all channels globally.
        :param source: The GUID, name, or project path of the Audio Source to get the min and max peaks from.
        :param time_from: The start time, in seconds, of the section of the audio source for which peaks are required.
                          This number must be smaller than timeTo. Range: [0,*]
        :param time_to: The end time, in seconds, of the section of the audio source for which peaks are required. This
                        number must be larger than timeFrom. Range: [0,*]
        :param num_peaks: The number of peaks that are required (minimum 1). Range: [1,4294967295]
        :param cross_channel_peaks: When true, peaks are calculated globally across channels, instead of per channel.
        :returns: A tuple containing the binary strings representing the peaks, the amount of channels, the maximum
                  absolute value, the length of the tuple, the size of the data in the tuple, and the description of
                  the channel configuration. **Refer to the Audiokinetic documentation for more detailed information**.
                  NOTE: if the call fails, this function will return an empty tuple.
        """
        time_from = max(time_from, 0)
        time_to = max(time_to, 0)
        num_peaks = max(num_peaks, 1)
        
        if time_from >= time_to:
            raise ValueError("The value of `time_from` must be smaller than the value of `time_to`.")
        
        args = {"object": f"{EObjectType.AUDIO_SOURCE}:{source}" if isinstance(source, Name) else source,
                "timeFrom": time_from, "timeTo": time_to, "numPeaks": num_peaks,
                "getCrossChannelPeaks": cross_channel_peaks}
        
        result = self._client.call("ak.wwise.core.audioSourcePeaks.getMinMaxPeaksInRegion", args)
        
        if result is None:
            return tuple[tuple[bytes, ...], int, float, float, float, str]()  # empty
        return (result["peaksBinaryStrings"], int(result["numChannels"]), result["maxAbsValue"],
                result["peaksArrayLength"], result["peaksDataSize"], result["channelConfig"])
    
    def get_min_max_peaks_in_trimmed_region(self, source: GUID | Name | ProjectPath, num_peaks: int,
                                            cross_channel_peaks: bool = False) -> tuple[
        tuple[bytes, ...], int, float, float, float, str]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_audiosourcepeaks_getminmaxpeaksintrimmedregion.html \n
        Gets the min/max peak pairs in the entire trimmed region of an audio source, for each channel, as an array of
        binary strings (one per channel). The strings are base-64 encoded, 16-bit signed int arrays, with min and max
        values being interleaved. If getCrossChannelPeaks is true, there is only one binary string representing peaks
        across all channels globally.
        :param source: The GUID, name, or project path of the Audio Source to get the min and max peaks from.
        :param num_peaks: The number of peaks that are required (minimum 1). Range: [1,4294967295]
        :param cross_channel_peaks: When true, peaks are calculated globally across channels, instead of per channel.
        :returns: A tuple containing the binary strings representing the peaks, the amount of channels, the maximum
                  absolute value, the length of the tuple, the size of the data in the tuple, and the description of
                  the channel configuration. **Refer to the Audiokinetic documentation for more detailed information**.
                  NOTE: if the call fails, this function will return an empty tuple.
        """
        num_peaks = max(num_peaks, 1)
        
        args = {"object": f"{EObjectType.AUDIO_SOURCE}:{source}" if isinstance(source, Name) else source,
                "numPeaks": num_peaks, "getCrossChannelPeaks": cross_channel_peaks}
        
        result = self._client.call("ak.wwise.core.audioSourcePeaks.getMinMaxPeaksInTrimmedRegion", args)
        
        if result is None:
            return tuple[tuple[bytes, ...], int, float, float, float, str]()  # empty
        return (result["peaksBinaryStrings"], int(result["numChannels"]), result["maxAbsValue"],
                result["peaksArrayLength"], result["peaksDataSize"], result["channelConfig"])
