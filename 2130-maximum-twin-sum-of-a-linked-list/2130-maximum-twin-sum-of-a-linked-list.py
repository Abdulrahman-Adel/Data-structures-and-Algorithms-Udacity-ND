# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        prefix = []
        sufix = []
        current = head
        while current:
            n += 1
            current = current.next

        i = 0
        print('Length: ', n)
        print('Half: ', (n // 2) - 1)
        while head:
            if 0 <= i <= (n // 2) - 1:
                prefix.append(head.val)
            else:
                sufix.append(head.val)
            head = head.next
            i+=1
        
        print('prefix: ', prefix)
        print('suffix: ', sufix)
        return max([s+p for p, s in zip(prefix, sufix[::-1])])