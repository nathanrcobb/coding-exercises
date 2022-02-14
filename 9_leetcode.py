"""
Palindrome Number
=================

https://leetcode.com/problems/palindrome-number/submissions/

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""
debug = False


class Solution:    
    def isPalindrome(self, x: int) -> bool:
        # Cast int to a string
        s = str(x)
        isP = True
        
        # Base case
        if len(s) == 1:
            return True
        
        # Check if the string is a palindrome
        # Odd-length palindrome
        elif len(s) % 2 == 1:
            center = len(s) // 2
            for i in range(0,center+1):
                if debug: print("%s ?= %s" %(s[center-i], s[center+i]))
                if s[center-i] != s[center+i]:
                    isP = False
                    break
            
        # Even-length palindrome
        else:
            center = len(s) // 2
            for i in range(0,center):
                if s[(center-1)-i] != s[center+i]:
                    isP = False
                    break
                
        return isP