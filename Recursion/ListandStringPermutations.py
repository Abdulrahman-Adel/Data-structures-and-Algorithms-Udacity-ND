# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:21:57 2020

@author: Abdelrahman
"""
lis = []

def permute(l):
    global lis
    if len(l) <= 1:
        return [l]
    elif len(l) == 2:
        return [[l],l[::-1]]
    else:
        output = []
        current_level = l[0]
        prev_level = permute(l[1:])

        for element in prev_level:  # For each answer from previous level
            for pos in range(len(element) + 1):  # For each possible position to put this level value
                temp_list = []
                temp_element = element.copy()
                for i in range(len(element) + 1):
                    if pos == i:
                        temp_list.append(current_level)
                    else:
                        temp_list.append(temp_element.pop())
                output.append(temp_list)
        return output
    
    
    