class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans: List[int] = []
        start, end = 0, k
        while end < len(nums) + 1:
            ans.append(max(nums[start:end]))
            start, end = start + 1, end + 1
        return ans
