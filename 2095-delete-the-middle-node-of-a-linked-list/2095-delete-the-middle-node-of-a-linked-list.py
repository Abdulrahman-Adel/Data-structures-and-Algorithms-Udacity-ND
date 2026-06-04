# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1

        current = head
        while current.next:
            length += 1
            current = current.next
        
        prev = None
        current = head
        midpoint = length//2
        print(length)
        if length == 1:
            head = None
            return head
        print(midpoint)
        for i in range(midpoint):
            prev = current
            current = current.next
            if i == midpoint-1:
                if current:
                    if current.next:
                        prev.next = current.next
                    else:
                        prev.next = None
                else:
                    prev.next = None
            

        return head