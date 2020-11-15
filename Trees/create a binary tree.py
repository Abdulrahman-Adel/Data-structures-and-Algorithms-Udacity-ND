# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:28:43 2020

@author: Abdelrahman
"""

class Node(object):
    def __init__(self,value = None, right = None, left = None):
        self.value = value
        self.right = right
        self.left = left
        
    def get_value(self):
        return self.value
    
    def set_value(self,value):
        self.value = value
        
    def set_left_child(self,node):
        self.left = node
    
    def get_left_child(self):
        return self.left
    
    def set_right_child(self,node):
        self.right = node    
        
    def get_right_child(self):
        return self.right
    
    def has_right_child(self):
        return self.right != None
    
    def has_left_child(self):
        return self.left != None
    

class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    
        
        