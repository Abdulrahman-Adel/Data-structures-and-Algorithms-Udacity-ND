# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # So this is my non-elegant solution it's simple just first tranverse the list and get the acutall length and then after that go through the list one more time when ever you get to the middle just remove the pointer from prev to current to current.next and that's it 
        # length = 1

        # current = head
        # while current.next:
        #     length += 1
        #     current = current.next
        
        # prev = None
        # current = head
        # midpoint = length//2
        # if length == 1:
        #     head = None
        #     return head
        # for i in range(midpoint):
        #     prev = current
        #     current = current.next
        #     if i == midpoint-1:
        #         if current:
        #             if current.next:
        #                 prev.next = current.next
        #             else:
        #                 prev.next = None
        #         else:
        #             prev.next = None
        # return head

        # Another very smart approach is basically to use two pointers the thing here is that one pointer is moving twice as fast as the other one so that means whenever the fast pointer reaches to the end of the list the slow pointer will be in the middle 

        prev = None
        fast = head
        slow = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if not prev:
            head = None
            return head
        if slow:
            prev.next = slow.next
        else:
            prev.next = None
        if fast:
            print(fast.val)
        print(slow.val)
        return head