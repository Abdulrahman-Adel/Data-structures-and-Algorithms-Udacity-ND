class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        ops = 0
        
        for num in nums:
            if hashmap[k-num] > 0:
                ops += 1
                hashmap[k-num] -= 1
            else:
                hashmap[num] += 1
                
        return ops