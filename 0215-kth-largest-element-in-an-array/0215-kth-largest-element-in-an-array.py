class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap and priority queue are the same thing 
        # just a special form of binary tree represening element in hirarchy bases on priority
        # by default pythons heap is a min heap (root is the minumum and as you go down the numbers increase)
        # find the kth element just convert array into heap O(n) operation and loop into k and pop to get the kth
        # since it's min heap we need to conver it into max heap first (python doesn't support max heap)
        # so the easiest solution is just to convert all number in the array first by -1 so then it's automatically max
        import heapq
        nums = [n*-1 for n in nums] # to make is max heap
        heapq.heapify(nums)

        for i in range(k):
            element = heapq.heappop(nums)
            if i==k-1:
                return element * -1 # revert back


