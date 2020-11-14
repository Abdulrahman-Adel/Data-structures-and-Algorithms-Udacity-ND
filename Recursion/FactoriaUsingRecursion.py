# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:40:03 2020

@author: Abdelrahman
"""

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
print ("Pass" if (1 == factorial(0)) else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
print ("Pass" if  (120 == factorial(5)) else "Fail")