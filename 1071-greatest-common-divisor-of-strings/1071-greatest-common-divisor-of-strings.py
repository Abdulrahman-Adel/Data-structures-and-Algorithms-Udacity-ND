class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            smallerword, biggerword = str1, str2
        else:
             smallerword, biggerword = str2, str1
        finalsubstring = ''
        for i in range(len(smallerword)):
            substring=smallerword[:i+1]
            if (substring * (len(smallerword) // len(substring))==smallerword) and (substring * (len(biggerword) // len(substring))==biggerword):
                finalsubstring = substring 
        return finalsubstring