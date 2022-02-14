"""
Reverse Integer
===============

https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21
 
Constraints:

-231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        
        # Remember if negative
        if x < 0:
            negative = True
            x = x * -1
        
        # Cast int to a string
        s = str(x)
        
        # Reverse string
        s = s[::-1]
        
        # Try to cast back to int; if error, return 0
        try:
            y = int(s)
            if y > (2**31-1):
                return 0
        except:
            return 0
        
        if negative:
            y = y * -1
            
        return y