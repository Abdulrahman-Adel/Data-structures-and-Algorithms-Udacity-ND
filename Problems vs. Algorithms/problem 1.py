# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:36:32 2020

@author: Abdelrahman
"""

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None
    if number ==0 or number == 1:
        return number
    
    start = 0
    end = number // 2
    
    while start <= end:
        mid = (start + end) // 2
        mid_pow = mid**2
        
        if mid_pow == number:
            return mid
        
        elif mid_pow < number:
            start = mid +1
            result = mid
        else:
            end  = mid -1
    
    return result

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


print('\nEdge Cases:')
print("Pass" if (None == sqrt(-3)) else "Fail")
print("Pass" if (99380 == sqrt(9876543210)) else "Fail")
