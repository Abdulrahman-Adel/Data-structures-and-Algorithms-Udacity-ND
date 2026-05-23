class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # this for some reason got time limited (I think maybe the problem is with assigning a subarray each iteration)
        # max_avg = float('-inf')
        # for i in range(len(nums)-k+1):
        #     subarray = nums[i: i+k]
        #     avg = sum(subarray)
        #     max_avg = max(max_avg, avg)
        
        # return max_avg/k

        # maybe a simpler solution is just define the first sub array and just substract and add to the existing sum

        windowed_sum = sum(nums[:k])
        max_sum = windowed_sum

        for i in range(k, len(nums)):
            windowed_sum = windowed_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, windowed_sum)
        
        return max_sum / k
