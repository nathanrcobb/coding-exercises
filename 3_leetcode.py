"""
Longest Substring Without Repeating Characters
==============================================

https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        # Base case
        if len(s) == 1:
            return 1
        for i in range(len(s)+1):
            for j in range(i,len(s)+1):
                substr = s[i:j]
                if len(set(substr)) == len(substr):
                    if len(substr) > len(longest):
                        longest = substr
                else:
                    i = j
                    break
        return len(longest)