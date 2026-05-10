class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowles = 'aeiou'
        # vowlesIndecies = []
        # vowlesInS = []
        # sList = [char for char in s]
        # for i in range(len(s)):
        #     if s[i].lower() in vowles:
        #         vowlesIndecies.append(i)
        #         vowlesInS.append(s[i])

        # for j in range(len(vowlesIndecies)):
        #     sList[vowlesIndecies[j]] = vowlesInS[len(vowlesIndecies)-1-j]
        # return ''.join(sList)
        # vowles = 'aeiou'

        # stack = []
        # for char in s:
        #     if char.lower() in vowles:
        #         stack.append(char)
        
        # finalword = ''
        # for char in s:
        #     if char.lower() in vowles:
        #         finalword += stack.pop()
        #     else:
        #         finalword += char
        # return finalword
        #########  Third Solution ################
        ########### Two pointers ###############
        """
        I c e C r e A m
        ^             ^   → both vowels (I, m? no) → left=I, right skips m,A
        I c e C r e A m
        ^           ^     → swap I and A
        A c e C r e I m
        ^       ^       → left skips c, right skips I... wait I is vowel
        A c e C r e I m
            ^     ^       → swap e and I  ... and so on
        """
        vowles = 'aeiou'
        left, right = 0, len(s) - 1
        sList = list(s)
        while left < right:
            
            while left < right and s[right].lower() not in vowles:
                right -= 1
            
            while left < right and s[left].lower() not in vowles:
                left += 1

            sList[left], sList[right] = sList[right], sList[left]
            left += 1 
            right -= 1
        return ''.join(sList)         



