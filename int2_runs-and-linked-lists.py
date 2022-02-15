# Given an array of unsorted positive integers, write a function that finds runs
# of 3 consecutive numbers (ascending or descending) and returns the indices where
# such runs begin. 
# If no such runs are found, return null.
# Include a minimal unit test suite for your function.

# ## example.```text
# findConsecutiveRuns(input: Array) -> Optional[Array]
# Input:  [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7]
# Output: [0, 4, 6, 7]

# Input:  [2, 5, 9]
# Output: None

"""
def checkForRun(check:list) -> bool:
    if check[0] == check[1] - 1 and check[2] == check[1] + 1:
        return True
    elif check[0] == check[1] + 1 and check[2] == check[1] - 1:
        return True
        
    return False

def findConsecutiveRuns(input:list) -> (int, int, int):
    retVal = []
    
    # Try brute force first
    for i in range(1,len(input)-1):
        if checkForRun([input[i-1], input[i], input[i+1]]):
            retVal.append(i-1)
    
    print(retVal)
    return retVal

if findConsecutiveRuns([1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7]) == [0, 4, 6, 7]:
    print("First test passed")
else:
    print("First test failed")
    
if findConsecutiveRuns([2, 5, 9]) == None:
    print("Second test passed")
else:
    print("Second test failed")
    
if findConsecutiveRuns([2, 5]) == None:
    print("Third test passed")
else:
    print("Third test failed")
"""   

class Node:
    def __init__(self,val:int):
        self.val = val
        self.next = None

def printList(node:Node):
    if node == None:
        return None
    
    printList(node.next)
    
    print(node.val)

#class LinkedList:
#    def __init__(self,

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

printList(n1)