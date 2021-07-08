"""
Write a Python function that returns the sublist of strings in aList that 
contain fewer than 4 characters. For example,
if aList = ["apple", "cat", "dog", "banana"],
your function should return: ["cat", "dog"]
"""
def lessThan4(aList):
    '''
    aList: a list of strings
    '''   
    subList =[]               #definging a empty list for adding  words with fewer than 4 characters
    for i in aList:           #defining i as the words in aList
        if len(i)<4:          #if the word is fewer than 4 characters, adding this word to sublist
            subList.append(i)
    return subList