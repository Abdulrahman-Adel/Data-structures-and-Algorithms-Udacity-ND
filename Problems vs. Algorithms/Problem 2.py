# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 16:32:59 2020

@author: Abdelrahman
"""

def findPivot(arr, low, high): 
      
    if high < low: 
        return -1
    if high == low: 
        return low 
       
    mid = (low + high) // 2 
      
    if mid < high and arr[mid] > arr[mid + 1]: 
        return mid 
    if mid > low and arr[mid] < arr[mid - 1]: 
        return (mid-1) 
    if arr[low] >= arr[mid]: 
        return findPivot(arr, low, mid-1) 
    return findPivot(arr, mid + 1, high) 

def binarySearch(arr, low, high, key): 
  
    if high < low: 
        return -1
               
    mid = (low + high) // 2 
      
    if key == arr[mid]: 
        return mid 
    if key > arr[mid]: 
        return binarySearch(arr, (mid + 1), high, key)
    return binarySearch(arr, low, (mid -1), key)

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = findPivot(input_list, 0, len(input_list)-1); 
  
    if pivot == -1: 
        return binarySearch(input_list, 0, len(input_list)-1, number)
  

    if input_list[pivot] == number: 
        return pivot 
    if input_list[0] <= number: 
        return binarySearch(input_list, 0, pivot-1, number)
    return binarySearch(input_list, pivot + 1, len(input_list)-1, number) 
        
        

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])