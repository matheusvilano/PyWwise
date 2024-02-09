from waapi import WaapiClient as _WaapiClient


class AudioSourcePeaks:
    """ak.wwise.core.audioSourcePeaks"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def get_min_max_peaks_in_region(self):
        """
        Gets the min/max peak pairs, in the given region of an audio source, as a collection of binary
        strings (one per channel). The strings are base-64 encoded, 16-bit signed int arrays,
        with min and max values being interleaved. If getCrossChannelPeaks is true, only one binary
        string represents the peaks across all channels globally.
        """

    def get_min_max_peaks_in_trimmed_region(self):
        """
        Gets the min/max peak pairs in the entire trimmed region of an audio source, for each channel,
        as an array of binary strings (one per channel). The strings are base-64 encoded, 16-bit signed
        int arrays, with min and max values being interleaved. If getCrossChannelPeaks is true,
        there is only one binary string representing peaks across all channels globally.
        """
