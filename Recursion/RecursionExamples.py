# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:29:36 2020

@author: Abdelrahman
"""

def sum_inegers(n):
    if n <= 1:
        return 1
    else:
        return n + sum_inegers(n-1)
    
print(sum_inegers(10))    


def sum_array(array):
    if len(array) == 1:
        return array[0]
    
    return array[0] + sum_array(array[1:])

arr = [1, 2, 3, 4]
print(sum_array(arr))

""" Looking at this, you might think it has a running time of O($n$),
 but that isn't correct due to the slice operation array[1:].
 This operation will take O($k$) time to run where $k$ is the number of elements to copy.
 So, this function is actually O($k*n$) running time complexity and O($k*n$) space complexity.
""" 


def sum_array_index(array, index):
    # Base Cases
    if len(array) - 1 == index:
        return array[index]
    
    return array[index] + sum_array_index(array, index + 1)

arr = [1, 2, 3, 4]
print(sum_array_index(arr, 0))

"""
Instead of slicing, we can pass the index for the element that we want to use for addition.
 That will give us the above function
"""