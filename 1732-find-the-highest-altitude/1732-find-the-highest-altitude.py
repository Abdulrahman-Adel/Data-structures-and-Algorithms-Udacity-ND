class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0]
        for i in range(len(gain)):
            prefix.append(gain[i] + prefix[i])
        return max(prefix)