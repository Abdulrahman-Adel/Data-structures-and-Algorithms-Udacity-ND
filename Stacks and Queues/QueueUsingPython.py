# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:42:07 2020

@author: Abdelrahman
"""

class Queue:
    def __init__(self):
         # TODO: Initialize the Queue
            self.arr = []
    
    def size(self):
         # TODO: Check the size of the Queue
        return len(self.arr)
    
    def enqueue(self, item):
         # TODO: Enter item into Queue
        self.arr.append(item)
            
    def dequeue(self):
         # TODO: Remove item from the Queue
        return self.arr.pop(0)