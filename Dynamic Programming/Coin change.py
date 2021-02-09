# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 17:35:57 2021

@author: Abdelrahman
"""

def return_change(memory: dict, coins: list, amount: int) -> int:
    """
    Returns the minimum given number of coins required to reach an amount
    :param memory: information about previous calculated cases
    :param coins: coins available to reach the amount
    :param amount: amount to reach
    :return: minimum number of coins to reach this amount
    """
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    if amount not in memory:
        memory[amount] = min(return_change(memory, coins, amount - c) + 1 for c in coins)

    return memory[amount]


def coin_change(coins: list, amount: int) -> int:
    """
    Given an amount and the coins available, indicates the minimum number of coins to reach this amount
    :param coins: coins available, may be used several times
    :param amount: amount to reach
    :return: minimum number of coins to reach the given amount
    """
    memory = {}

    change = return_change(memory=memory, coins=coins, amount=amount)

    if change == float('inf'):
        return -1
    else:
        return change
    
    
def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
        
        
arr = [1,2,5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)


arr = [1,4,5,6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)


arr = [5,7,8]
amount = 2   
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)