class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        for i in range(1, len(s)):
            if s[i] in s[start:i]:
                max_len = max(i - start, max_len)
                while s[start] != s[i]:
                    start += 1
                start += 1
                continue
                
        max_len = max(len(s) - start, max_len)
        
        return max_len