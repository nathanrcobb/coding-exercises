"""
Templates
=========

This file's purpose is to provide examples of how to use classes, data structures, and
other techniques in Python.

References:
https://www.geeksforgeeks.org/python-data-structures-and-algorithms/
"""

"""
Classes
-------


"""

"""
Data Structures
---------------
1) Lists
  Python Lists are ordered collections of data just like arrays in other programming languages. It allows different types of elements in the list. The implementation of Python List is similar to Vectors in C++ or ArrayList in JAVA. The costly operation is inserting or deleting the element from the beginning of the List as all the elements are needed to be shifted. Insertion and deletion at the end of the list can also become costly in the case where the preallocated memory becomes full.
"""
# Definition of a list
l = ['t','e','s','t','l','i','s','t']


"""
2) Tuples
  Python tuples are similar to lists but Tuples are immutable in nature i.e. once created it cannot be modified. Just like a List, a Tuple can also contain elements of various types.

  In Python, tuples are created by placing a sequence of values separated by a comma with or without the use of parentheses for grouping of the data sequence.
"""

"""
3) Sets
  Python set is a mutable collection of data that does not allow any duplication. Sets are basically used to include membership testing and eliminating duplicate entries. The data structure used in this is Hashing, a popular technique to perform insertion, deletion, and traversal in O(1) on average. 

  If Multiple values are present at the same index position, then the value is appended to that index position, to form a Linked List. In, CPython Sets are implemented using a dictionary with dummy variables, where key beings the members set with greater optimizations to the time complexity.
"""

"""
4) Frozen Sets
  Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation.
"""
"""
5) Dictionaries
  Python dictionary is an unordered collection of data that stores data in the format of key:value pair. It is like hash tables in any other language with the time complexity of O(1). Indexing of Python Dictionary is done with the help of keys. These are of any hashable type i.e. an object whose can never change like strings, numbers, tuples, etc. We can create a dictionary by using curly braces ({}) or dictionary comprehension.
"""

"""
6) Linked Lists
---------------
  A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers, each with an associated value.

  A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL. Each node in a list consists of at least two parts:
    -Data
    -Pointer (Or Reference) to the next node
"""
# Node class
class Node:
  
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null
  
  
# Linked List class contains a Node object
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
    # This function prints contents of linked list starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
  
  
# Code execution starts here
if __name__=='__main__':
  
    # Start with the empty list
    llist = LinkedList()
  
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
  
    llist.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node
  
    llist.printList()

"""
7) Stack (collections.deque)
  A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.

  The functions associated with stack are:
    -empty(): Returns whether the stack is empty [Time Complexity: O(1)]
    -size(): Returns the size of the stack [Time Complexity: O(1)
    -top(): Returns a reference to the topmost element of the stack [Time Complexity: O(1)]
    -append(a): Inserts the element 'a' at the top of the stack [Time Complexity: O(1)]
    -pop(): Deletes the topmost element of the stack [Time Complexity: O(1)]
"""

from collections import deque
stack = deque

"""
8) Queue
  As a stack, the queue is a linear data structure that stores items in a First In First Out (FIFO) manner. With a queue, the least recently added item is removed first. A good example of the queue is any queue of consumers for a resource where the consumer that came first is served first.

  Operations associated with queue are:
    -Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition [Time Complexity: O(1)]
    -Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition [Time Complexity: O(1)]
    -Front: Get the front item from queue [Time Complexity: O(1)]
    -Rear: Get the last item from queue [Time Complexity: O(1)]
"""


"""
9) Heap
  heapq module in Python provides the heap data structure that is mainly used to represent a priority queue. The property of this data structure is that it always gives the smallest element (min heap) whenever the element is popped. Whenever elements are pushed or popped, heap structure is maintained. The heap[0] element also returns the smallest element each time. It supports the extraction and insertion of the smallest element in the O(log n) times.

  Generally, Heaps can be of two types:

  Max-Heap: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
  Min-Heap: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. The same property must be recursively true for all sub-trees in that Binary Tree.
"""


"""
10) Binary Tree
  A tree is a  hierarchical data structure. The topmost node of the tree is called the root whereas the bottommost nodes or the nodes with no children are called the leaf nodes. The nodes that are directly under a node are called its children and the nodes that are directly above something are called its parent.

  A binary tree is a tree whose elements can have almost two children. Since each element in a binary tree can have only 2 children, we typically name them the left and right children. A Binary Tree node contains the following parts.
    -Data
    -Pointer to left child
    -Pointer to the right child
"""