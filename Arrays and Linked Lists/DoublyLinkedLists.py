# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:27:36 2020

@author: Abdelrahman
"""

class DoubleNode:
    def __init__(self,data):
        self.head = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init(self):
        self.head = None
        self.tail = None
    
    def append(self,value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        else:
            self.tail.next = DoubleNode(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        return    
    
    def remove(self,value):
        if self.head == value:
            self.head = self.head.next
            return
            
        tail = self.head
        prev_tail = None
        while tail:
            if tail.next == value:
                prev_tail.next = tail.next
            prev_tail = tail    
            tail = tail.next    
            
    def pop(self):
         value = self.head
         self.remove(value)
         return value
    
    def insert(self,value,pos):
        tail = self.head
        self.counter = 0
        while tail:
            if self.counter == pos:
                data = tail
                tail = DoubleNode(value)
                tail.next = data
                return
            tail = tail.next              
            