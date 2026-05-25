class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowles = 'aeiou'
        max_vowles = 0
        for i in range(k):
            if s[i] in vowles:
                max_vowles += 1
        
        count = max_vowles
        for j in range(k, len(s)):
            if s[j] in vowles:
                count += 1
            if s[j-k] in vowles:
                count -= 1
            
            max_vowles= max(max_vowles, count)

        return max_vowles