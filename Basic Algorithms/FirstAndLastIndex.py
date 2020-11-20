# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:59:39 2020

@author: Abdelrahman
"""

def Binary_search(arr,target_value,index_ref=0):
    center = (len(arr)-1)//2 
    if len(arr) == 0:
       return None
    if arr[center] == target_value:
        return index_ref + center
    elif arr[center] > target_value:
        return Binary_search(arr[:center],target_value,index_ref)
    else :
        return Binary_search(arr[center+1:],target_value,index_ref+center+1) 
    
def find_first(arr,target):
    index = Binary_search(arr,target)
    if index == 0:
            return index
    if not index:
        return -1
    indecies = [index]    
    while index:
        index = Binary_search(arr[:index],target)
        if index:
            indecies.append(index)
    if len(indecies) >= 1:
        return min(indecies)
    else:
        return -1  
    
def find_last(arr,target):
    index = Binary_search(arr,target)
    if index == len(arr)-1:
            return index 
    if not index:
        return -1    
    indecies = [index]    
    while index:
        index = Binary_search(arr[index+1:],target,index+1)
        if index:
            indecies.append(index)
    if len(indecies) > 1:
        return max(indecies)
    else:
        return -1      
    
input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3    
input_list = [1]
number = 1
input_list = [0, 1, 2, 3, 4, 5]
number = 5
input_list = [0, 1, 2, 3, 4, 5]
number = 6
print([find_first(input_list,number),find_last(input_list,number)])    


def find_first_sol(target, source):
    index = Binary_search(target, source)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index   
        
def find_last_sol(target, source):
    upper_index = Binary_search(target, source)
    while source[upper_index] == target:
        if upper_index == len(source) - 1:
            upper_index = len(source) - 1
            break
        if source[upper_index + 1] == target:
            upper_index += 1
        else:
            return upper_index        