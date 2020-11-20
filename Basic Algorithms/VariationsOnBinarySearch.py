# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:33:54 2020

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
    indecies = [index]    
    while index:
        index = Binary_search(arr[:index],target)
        if index:
            indecies.append(index)
    if len(indecies) > 1:
        return min(indecies)
    else:
        return None        

    
multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(multiple,7)) # Should return 3
print(find_first(multiple,9)) # Should return None


def contains(arr,target):
    return Binary_search(arr,target) is not None

letters = ['a', 'c', 'd', 'f', 'g']
print(contains(letters,'a')) ## True
print(contains(letters,'b')) ## False