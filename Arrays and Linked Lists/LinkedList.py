# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:37:20 2020

@author: Abdelrahman
"""

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def PrintList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
   
    def append(self,value):
        if self.head == None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return
   
    def to_list(self):
        node_values = []
        node = self.head
        while node:
            node_values.append(node.value)
            node = node.next
        return node_values
    
def create_linked_list_better(input_list):
        """
        Function to create a linked list, improved performance
        @param input_list: a list of integers
        @return: head node of the linked list
        """
        head = None
        tail = None
        
        for value in input_list:
            
            if head is None:
                head = Node(value)
                tail = head # when we only have 1 node, head and tail refer to the same node
            else:
                tail.next = Node(value) # attach the new node to the `next` of tail
                tail = tail.next # update the tail
            
        return head            
        
if __name__ == "__main__":
    
    llist = LinkedList()
    
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    
    ##llist.PrintList()

    
    input_list = [1, 2, 3, 4, 5, 6]
    
    linedlist = create_linked_list_better(input_list)