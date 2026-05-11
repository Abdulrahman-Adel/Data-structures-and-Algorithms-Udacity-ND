class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1] * len(nums)
        rightProducts = [1] * len(nums)
        for i in range(1, len(nums)):
            leftProducts[i] = leftProducts[i-1] * nums[i-1]
        for j in range(len(nums) - 2, -1, -1):
            rightProducts[j] = rightProducts[j+1] * nums[j+1]
        return [x*y for x, y in zip(leftProducts, rightProducts)]