class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split()

        left, right = 0, len(sList)-1

        while left < right:
            sList[left], sList[right] = sList[right], sList[left]
            left += 1
            right -= 1
        
        return ' '.join(sList).strip()