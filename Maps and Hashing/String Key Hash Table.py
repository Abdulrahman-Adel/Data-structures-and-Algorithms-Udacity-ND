# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 00:39:40 2020

@author: Abdelrahman
"""

class HashTable(object):
    def __init__(self):
        self.p = 100
        self.bucket_array = []

    def calculate_hash_value(self,string):
        return ord(string[0])*self.p + ord(string[1])
    
    def lookup(self,key):
        if self.calculate_hash_value(key) in self.bucket_array:
            return self.calculate_hash_value(key)
        else:
            return -1
        
    def store(self,key):
        self.bucket_array += [self.calculate_hash_value(key)]
        
        
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))        
        
        
        
    