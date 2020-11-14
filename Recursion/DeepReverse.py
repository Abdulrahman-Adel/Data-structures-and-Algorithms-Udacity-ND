# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:43:19 2020

@author: Abdelrahman
"""

def deep_reverse(l):
    if type(l) is not list:
        return l
    else:
        result = []
        l = l[::-1]
        for element in l:
            result.append(deep_reverse(element))
        return result

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")    
        
arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)        