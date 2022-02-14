"""
Longest Palindromic Substring
=============================

https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def checkForPalindrome(self, s: str, i: int) -> str:
        longestOdd = ""
        longestEven = ""
        # Base case
        if len(s) == 0:
            return ""
        else:
            # Check for odd-length palindrome case
            j = 1
            longestOdd = s[i]
            if i >= 1 and i < len(s):
                while(i-j >= 0 and i+j < len(s)):
                    if s[i - j] == s[i + j]:
                        longestOdd = s[i-j] + longestOdd + s[i+j]
                    else:
                        break
                    j += 1
            # Check for even-length palindrome case
            j = 0
            while(i-j >= 0 and (i+1)+j < len(s)):
                if s[i-j] == s[(i+1)+j]:
                    longestEven = s[i-j] + longestEven + s[(i+1)+j]
                else:
                    break
                j += 1
        if len(longestEven) > len(longestOdd):
            longest = longestEven
        else:
            longest = longestOdd
        return longest
    
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(0,len(s)):
            temp = self.checkForPalindrome(s, i)
            if len(temp) > len(longest):
                longest = temp
        return longest
            
            
"""
Brute Force: Times out due to O(n^3)
    def checkIfPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False
        elif len(s) % 2 == 1:
            pivot = len(s) // 2
            s1 = s[:pivot]
            s2 = s[pivot+1:]
            if s1 == s2[::-1]:
                #print("%s is a palindrome." %(s))
                return True
        else:
            pivot = len(s) // 2
            s1 = s[:pivot]
            s2 = s[pivot:]
            if s1 == s2[::-1]:
                #print("%s is a palindrome." %(s))
                return True
        return False
    
    def longestPalindrome(self, s: str) -> str:
        # Base case 
        if len(s) == 1:
            return s
        elif len(s) == 2:
            if self.checkIfPalindrome(s):
                return s
            else:
                return s[0]
        else:
            longest = ""
            for i in range(len(s)+1):
                for j in range(i,len(s)+1):
                    if self.checkIfPalindrome(s[i:j]) and len(s[i:j]) > len(longest):
                        longest = s[i:j]
            return longest
"""