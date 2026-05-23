class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute-force Memory Limit Exceeded
        # storage = []
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         storage.append(min(height[i], height[j]) * (j-i))
        # return max(storage)


        # the idea here is to use two pointers
        # the actual main idea is that you should move the pointer with the lowest hight only since the other one might give you the best (largest) area

        left, right  =  0, len(height) - 1
        
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right -  left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1                
        return max_area


            