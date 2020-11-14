# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:42:05 2020

@author: Abdelrahman
"""

def reverse_string(input):
    if len(input) <= 1:
        return input
    else:
        return input[-1] + reverse_string(input[:-1])
    
print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("gnirts" == reverse_string("string")) else "Fail")


def is_palindrome(input):
    return reverse_string(input) == input 

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")    