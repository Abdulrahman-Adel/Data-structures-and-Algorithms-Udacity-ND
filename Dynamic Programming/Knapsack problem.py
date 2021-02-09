# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:59:12 2021

@author: Abdelrahman
"""

import collections

Item = collections.namedtuple('Item', ['weight', 'value'])  

def max_value(knapsack_max_weight: int, n: int) -> int:
    """
    Get the maximum value of the knapsack.
    """
    
    if n == 0 or knapsack_max_weight == 0: 
        return 0
    
    if matrix[n][knapsack_max_weight] != -1: 
        return matrix[n][knapsack_max_weight] 
  
    # choice diagram code 
    if items[n-1][0] <= knapsack_max_weight: 
        matrix[n][knapsack_max_weight] = max( 
            items[n-1][1] + max_value(knapsack_max_weight-items[n-1][0], n-1), 
            max_value(knapsack_max_weight, n-1)) 
        return matrix[n][knapsack_max_weight] 
    elif items[n-1][0] > knapsack_max_weight: 
        matrix[n][knapsack_max_weight] = max_value(knapsack_max_weight, n-1) 
        return matrix[n][knapsack_max_weight] 
    
    


tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
    
for test in tests:
    n = len(test['input']['items'])
    items = test['input']['items']
    matrix = [[-1 for i in range(test['input']['knapsack_max_weight'] + 1)] for j in range(n + 1)]
    assert test['correct_output'] == max_value(test['input']['knapsack_max_weight'],n)    