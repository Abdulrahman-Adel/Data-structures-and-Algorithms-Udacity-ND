class Solution:
    def reverseVowels(self, s: str) -> str:
        vowles = 'aeiou'
        vowlesIndecies = []
        vowlesInS = []
        sList = [char for char in s]
        for i in range(len(s)):
            if s[i].lower() in vowles:
                vowlesIndecies.append(i)
                vowlesInS.append(s[i])

        for j in range(len(vowlesIndecies)):
            sList[vowlesIndecies[j]] = vowlesInS[len(vowlesIndecies)-1-j]
        return ''.join(sList)