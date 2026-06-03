from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        n = len(senate)

        for i in range(len(senate)):
            if senate[i]=='R':
                radiant.append(i)
            else:
                dire.append(i)
        

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"

        