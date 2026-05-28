class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        

        counter1 = {}
        for c in word1:
            counter1[c] = counter1.get(c, 0) + 1
        
        counter2 = {}
        for c in word2:
            counter2[c] = counter2.get(c, 0) + 1
        
        return (sorted(counter1.values())==sorted(counter2.values())) and (set(counter1.keys())==set(counter2.keys()))
