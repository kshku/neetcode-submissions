class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = dict()
        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        
        start, end = 0, len(s1)
        while end <= len(s2):
            freq_window = dict()
            for c in s2[start:end]:
                freq_window[c] = freq_window.get(c, 0) + 1
            
            if freq_window == freq:
                return True
            start += 1
            end += 1
        
        return False