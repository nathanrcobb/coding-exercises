"""
Template
===================================================================================
Description
"""

# All test cases
testCases = [
    (0, 0),
    (1, 1)
]

# The solution class, which defines the algorithm and helper functions
class Solution:
    # Helper function
    def helper(self, val: int) -> int:
        pass

    # Main algorithm
    def algorithm(self, val : int) -> int:
        pass

# Test the algorithm
def testIt() -> int:
    # Define the solution object for testing
    sol = Solution()
    
    # Iterate through all input and expected output test pairs
    for i, v in testCases:
        ans = sol.algorithm(i)
        # Run each test case
        if ans != v:
            print("*** Test failed! ***\nExpected: %s\nActual: %s" %(v,ans))

    return 0

# Main, for easily running the algorithm/tests
if __name__ == "__main__":
    testIt()