# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:07:11 2020

@author: Abdelrahman
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

def iscircular(linked_list):
    slow_runner = linked_list.head
    fast_runner = linked_list.head.next
    while fast_runner:
        if slow_runner == fast_runner:
            return True
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
        
if __name__ == "__main__":
    list_with_loop = LinkedList([2, -1, 3, 0, 5])

    # Creating a loop where the last node points back to the second node
    loop_start = list_with_loop.head.next

    node = list_with_loop.head
    while node.next: 
        node = node.next   
    node.next = loop_start
    
    print ("Pass" if iscircular(list_with_loop) else "Fail")    