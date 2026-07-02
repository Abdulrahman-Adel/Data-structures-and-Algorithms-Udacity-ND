class Solution:
    def binarySearch(self, success, spell, potions):
        l, r = 0, len(potions) - 1

        smallet_more = None
        while l <= r:
            m = (l+r) // 2
            if potions[m] * spell>=success:
                # print(f'spell: {spell}, success: {success}, middle: {potions[m]}')
                smallet_more = m
                r = m - 1
            else:
                l = m + 1
        return smallet_more

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        final = []
        for s in spells:
            result = self.binarySearch(success, s, potions)
            if result is not None:
                # print(f'spell: {s}, success: {success}, potions: {potions[result:]}')
                final.append(len(potions) - result)
            else:
                final.append(0)
                
        return final 
            
