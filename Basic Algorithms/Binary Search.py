# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 19:47:11 2020

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
    
array = [ 2, 3, 4, 5,6, 7, 8, 9,10]
array = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
target_value = 7

print(Binary_search(array,target_value))    

        
