# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
from math import ceil
class Solution:
    def guessNumber(self, n: int) -> int:

        current_guess = ceil(n / 2)
        top = n
        bottom = 0
        while True:
            result = guess(current_guess)

            if result == 0:
                return current_guess
            elif result == -1:
                top = current_guess
                current_guess = ceil((current_guess + bottom) / 2)
            else:
                bottom = current_guess
                current_guess =  ceil((current_guess + top) / 2)
        
        return 0