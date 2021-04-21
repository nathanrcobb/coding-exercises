#!/usr/bin/env python
import sys,os

testRepositories = {
    1:  ["mobile","mouse","moneypot","monitor","mousepad"],
    2:  ["abcd", "njsafhsT", "isandabWBB", "hsfnKR", "aBbxkj", "YUGBJK", "NIUHNNN", "nkjndYB", "Abccd", "ABCDE"]
}
testExpectedResults = {
    1: [["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
    ],
    2: [["ABCDE"]
    ]
}

def search(repo, query):
    # Alphabetize the list
    tempList = []
    for x in repo:
        tempList += x.lower()
    repo = sorted(tempList)
    substrings = []
    results = []

    #print(repo)

    for i in range(1,len(query),1):
        substrings.append(query[0:i+1].lower())

    # Process each substring for a separate list
    for substring in substrings:
        temp = []
        #print(substring)
        # Process up to 3 word matches and return the list
        for word in repo:
            #print(word)
            if word[:len(substring)] == substring:
                temp.append(word)
                #print(temp)
            if len(temp) > 2:
                #print(temp)
                break
        results += [temp]

    # Print results
    #print(results)

    # List of lists of strings
    return results

def testSearch():
    if search(testRepositories[1], "mouse") is testExpectedResults[1]:
        print("Test 1 failed!")
    if search(testRepositories[2], "AB") is testExpectedResults[2]:
        print("Test 2 failed!")

if __name__ == '__main__':
    testSearch()