# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:12:51 2020

@author: Abdelrahman
"""

def mergesort(items):
    
    if len(items) <= 1:
        return items
    
    left = items[:len(items)//2]
    right = items[len(items)//2:]


    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)  


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
     

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def case_sort(string):

    lower_case_char = []
    upper_case_char = []

    for char in string:
        if ord(char) < 91:  # 90 is Z
            upper_case_char.append(char)
        else:
            lower_case_char.append(char)


    lower_case_char = mergesort(lower_case_char)
    upper_case_char = mergesort(upper_case_char)


    result = ''

    for char in string:
        if ord(char) < 91:  # 90 is Z
            result += upper_case_char.pop(0)
        else:
            result += lower_case_char.pop(0)

    return result


test_string = 'fedRTSersUXJ'
print(case_sort(test_string))