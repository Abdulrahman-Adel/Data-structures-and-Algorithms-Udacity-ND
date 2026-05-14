class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        pointer = 0
        for i in range(len(t)):
            if pointer == len(s):
                return True
            if t[i]==s[pointer]:
                pointer += 1
        return pointer==len(s)