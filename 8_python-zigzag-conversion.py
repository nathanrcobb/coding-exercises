"""
Zigzag Conversion
=================

https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""

debug = False

class Solution:
    def printScreen(self, screen):
        for row in screen:
            for col in row:
                print(col + " ", end="")
            print("")
        print("")
    
    def convert(self, s: str, numRows: int) -> str:
        # Calculate the screen width needed
        numCols = max(1,((len(s) // numRows)+(len(s) // 2)))
        
        screen = [[" " for j in range(numCols)] for i in range(numRows)]
        
        ix = 0
        col = 0
        while(ix < len(s)):
            for i in range(numRows):
                if ix >= len(s):
                    break;
                screen[i][col] = s[ix]
                ix += 1
                if debug: self.printScreen(screen)    
            col += 1
            for i in range(numRows-2, 0, -1):
                if ix == len(s):
                    break;
                screen[i][col] = s[ix]
                ix += 1
                col += 1
                if debug: self.printScreen(screen)
                
        temp = ""
        for row in screen:
            for c in row:
                if c != " ":
                    temp += c
        
        return temp