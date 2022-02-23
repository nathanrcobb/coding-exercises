"""
Multiples of 3 or 5 [Problem 1]
===================================================================================
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# All test cases
testCases = [
    (10, 23),
    (1000, 233168)
]

# The solution class, which defines the algorithm and helper functions
class Solution:
    # Helper function
    def getNaturalNumbersList(self, num: int) -> list:
        tempList = []

        # Generate the list of natural numbers divisible by 3 or 5
        for i in range(1,num):
            if i % 3 == 0 or i % 5 == 0:
                tempList.append(i)

        return tempList

    # Main algorithm
    def sumNaturalNumbersBelowVal(self, val : int) -> int:
        total = 0

        # Get the list of natural numbers
        numList = self.helper(val)

        # Sumb the list of natural numbers
        for i in numList:
            total += i

        return total

# Test the algorithm
def testIt():
    # Define the solution object for testing
    sol = Solution()
    
    # Iterate through all input and expected output test pairs
    for i, v in testCases:
        ans = sol.sumNaturalNumbersBelowVal(i)
        # Run each test case
        if ans != v:
            print("*** Test failed! ***\nExpected: %s\nActual: %s" %(v,ans))

# Main, for easily running the algorithm/tests
if __name__ == "__main__":
    testIt()