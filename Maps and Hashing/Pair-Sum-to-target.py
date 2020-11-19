# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 00:55:17 2020

@author: Abdelrahman
"""

import itertools

def pair_sum_to_zero(arr,target):
    list_of_sol = []
    for i in itertools.combinations(arr,2):
        if sum(i) == target:
            list_of_sol.append([arr.index(i[0]),arr.index(i[1])])
            
    return list_of_sol        

print(pair_sum_to_zero([10, 5, 9, 8, 12, 1, 16, 6], 16))

print(pair_sum_to_zero([0, 1, 2, 3, -4], -4))

"""
Another solution

def pair_sum_to_zero(input_list, target):
    index_dict = dict()
    for index, element in enumerate(input_list):
        if target - element in index_dict:
            return [index_dict[target - element], index]
        index_dict[element] = index
"""