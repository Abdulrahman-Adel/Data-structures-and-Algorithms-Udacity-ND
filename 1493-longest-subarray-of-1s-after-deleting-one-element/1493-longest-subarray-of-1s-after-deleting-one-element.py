class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prefix = 0
        suffix = 0
        max_adj = 0
        for i in range(len(nums)):
            if nums[i]==1:
                suffix +=1
            else:
                max_adj = max(max_adj, prefix+suffix)
                prefix = suffix
                suffix = 0
        if suffix == len(nums):
            suffix -= 1
        return max(max_adj, prefix+suffix)
            
