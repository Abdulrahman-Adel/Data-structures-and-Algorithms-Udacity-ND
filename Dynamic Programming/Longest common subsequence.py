# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:53:14 2021

@author: Abdelrahman
"""

def lcs(string_a: str, string_b: str) -> int:
    """
    Performs an unnormalized "longest common sequence" analysis of two strings
    :param string_a: a string
    :param string_b: another string
    :return: the length of the longest common sequence
    """
    m = len(string_a) 
    n = len(string_b) 
  
    
    matrix = [[None]*(n+1) for i in range(m+1)] 
    
  
    
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                matrix[i][j] = 0
            elif string_a[i-1] == string_b[j-1]: 
                matrix[i][j] = matrix[i-1][j-1]+1
            else: 
                matrix[i][j] = max(matrix[i-1][j] , matrix[i][j-1]) 
  
    
    return matrix[m][n] 

## Test cell

# Run this cell to see how your function is working
test_A1 = "WHOWEEKLY"
test_B1 = "HOWONLY"

lcs_val1 = lcs(test_A1, test_B1)

test_A2 = "CATSINSPACETWO"
test_B2 = "DOGSPACEWHO"

lcs_val2 = lcs(test_A2, test_B2)

print('LCS val 1 = ', lcs_val1)
assert lcs_val1==5, "Incorrect LCS value."
print('LCS val 2 = ', lcs_val2)
assert lcs_val2==7, "Incorrect LCS value."
print('Tests passed!')