# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 17:22:42 2021

@author: Abdelrahman
"""

def lps(input_string: str) -> int:
    """
    Given a string, returns the maximum palindrome lenght
    :param input_string: string to find palindromes on
    :return: maximum palindrom length
    """
    
    n = len(input_string)
    
    matrix = [[0 for x in range(n)] for x in range(n)]
    
    for i in range(n): 
        matrix[i][i] = 1
    
    #cl is the length of the substring
    for cl in range(2, n+1): 
        for i in range(n-cl+1): 
            j = i+cl-1
            if input_string[i] == input_string[j] and cl == 2: 
                matrix[i][j] = 2
            elif input_string[i] == input_string[j]: 
                matrix[i][j] = matrix[i+1][j-1] + 2
            else: 
                matrix[i][j] = max(matrix[i][j-1], matrix[i+1][j]); 
  
    return matrix[0][n-1] 



def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
        
string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)        


string = 'BANANA'
solution = 5
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)