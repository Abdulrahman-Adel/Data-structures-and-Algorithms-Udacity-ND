class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # hashmap = {}

        # for i in range(len(nums1)):
        #     hashmap[nums1[i]] = (1, True)

        # for i in range(len(nums2)):
        #     if hashmap.get(nums2[i]) and hashmap[nums2[i]][0] != 2:
        #         hashmap[nums2[i]] = (0, False)
        #     else:
        #         hashmap[nums2[i]] = (2, True)
        

        # answer = [[], []]
        # for key, value in hashmap.items():
        #     if value[1] ==True:
        #         answer[value[0] - 1].append(key)
        # return answer
        # A much simpler solution
        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1 - set2), list(set2 - set1)]
        
        