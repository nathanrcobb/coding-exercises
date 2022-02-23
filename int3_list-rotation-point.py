'''
List Rotation Point
====================================================================================
I want to learn some big words so people think I'm smart. I opened up the dictionary to a page in the middle and started flipping through, looking for words I didn't know. I put each word I didn't know at increasing indices in a huge array I created in memory. When I reached the end of the dictionary, I started from the beginning and did the same thing until I reached the page I started at.
Now I have an array of words that are mostly alphabetical, except they started somewhere in the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. In other words, this is an alphabetically ordered array that has been rotated.
Example:

var words = [
  'engender',
  'karpatka',
  'othellolagkage',
  'ptolemaic',
  'retrograde',
  'supplant',
  'undulate',
  'xenoepist',
  'asymptote', // <-- rotates here!
  'babka',
  'banoffee',
];

Write a function for finding the index of the “rotation point”, which is where I started working from the beginning of the dictionary. This array is huge (there are lots of words I don't know) so we want to be efficient.
'''

word_list = [ 
  'ptolemaic',
  'retrograde',
  'supplant',
  'undulate',
  'xenoepist',
  'asymptote',
  'babka',  
  'banoffee',
  'engender',
  'karpatka',
  'othellolagkage',
  ]

def findRotationPoint(word_list: list) -> int:
    found = -1
    start = 0
    end = len(word_list)
    
    
    if word_list[-1] > word_list[0]:
        return 0

    # Compare strings for recursion
    while(found < 0):
        halfway = start + ((end-start) // 2)
        
        # rotation point is in 2nd half
        if word_list[halfway - 1] > word_list[halfway]:
            found = halfway
        elif word_list[0] < word_list[halfway]:
            start = halfway
        else:
            end = halfway
        
    return found
    
print(findRotationPoint(word_list))