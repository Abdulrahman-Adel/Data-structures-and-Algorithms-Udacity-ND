class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ## the idea is to keep track of first and second numbers and when the third comes then true
        
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first  = num
            elif num <= second:
                second=num
            else:
                return True
        
        return False