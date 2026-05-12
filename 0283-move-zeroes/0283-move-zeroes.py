class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        zeroPointer = 0
        for i in range(len(nums)):
            if nums[i]==0:
                zeroPointer = i
                for j in range(i, len(nums)):
                    if nums[j] != 0:
                        nums[zeroPointer], nums[j] = nums[j], nums[zeroPointer]
                        zeroPointer += 1
        return nums