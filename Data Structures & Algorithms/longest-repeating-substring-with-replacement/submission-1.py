class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        freq_window = {}
        max_freq = 0
        max_size = 0

        for end in range(len(s)):
            freq_window[s[end]] = freq_window.get(s[end], 0) + 1
            max_freq = max(max_freq, freq_window[s[end]])

            while (end - start + 1) - max_freq > k:
                freq_window[s[start]] -= 1
                start += 1

            max_size = max(max_size, end - start + 1)

        return max_size