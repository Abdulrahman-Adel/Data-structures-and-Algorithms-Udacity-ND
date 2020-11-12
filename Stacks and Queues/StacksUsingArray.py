# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:59:29 2020

@author: Abdelrahman
"""

class Stack:
    
    def __init__(self,initialSize=10):
        self.arr = [0 for _ in range(initialSize)]
        self.next_index = 0
        self.num_elements = 0
        
    def push(self,value):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()
            
        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1
    
    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range( 2* len(old_arr))]
        for index, value in enumerate(old_arr):
            self.arr[index] = value  
       
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.next_index == 0
    
    def pop(self):
        if self.next_index == 0:
            return None
        
        self.next_index -= 1
        self.num_elements -= 1
        value  = self.arr[self.next_index]
        del self.arr[self.next_index]
        return value


if __name__ == "__main__":
    foo = Stack()
    foo.push("Test") # We first have to push an item so that we'll have something to pop
    print(foo.pop()) # Should return the popped item, which is "Test"
    print(foo.pop()) # Should return None, since there's nothing left in the stack