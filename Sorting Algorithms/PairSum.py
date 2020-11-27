# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:07:02 2020

@author: Abdelrahman
"""

def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    Return the two numbers in the form of a sorted list
    """

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                if arr[i] > arr[j]:
                    return [arr[j], arr[i]]
                else:
                    return [arr[i], arr[j]]

    return [None, None]

def test_function(test_case):
    input_list = test_case[0]
    target =test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")
        
#Test 1
input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)        
#Test 2 
input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
test_function(test_case)
#Test 3
input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
test_function(test_case)