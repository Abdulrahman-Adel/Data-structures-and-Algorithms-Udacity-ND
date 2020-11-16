# -*- coding: utf-8 -*-
"""
Problem Statement

A child is running up a staircase with and can hop either 1 step, 2 steps or 3 steps at a time.
If the staircase has n steps, 
write a function to count the number of possible ways in which child can run up the stairs.

"""

import functools
"""
this is a cashe which creates a thin wrapper around a dictionary lookup
for the function arguments. Because it never needs to evict old values.
"""
@functools.lru_cache(maxsize=None) 
def staircase(n):
    
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        climb_ways = 0
        climb_ways += staircase(n - 1)
        climb_ways += staircase(n - 2)
        climb_ways += staircase(n - 3)

        return climb_ways
    
    
print(staircase(5))    