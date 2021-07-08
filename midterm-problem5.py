"""
Write a Python function that returns a list of keys in aDict with the value 
target. The list of keys you return should be sorted in increasing order. 
The keys and values in aDict are both integers. (If aDict does not contain 
the value target, you should return an empty list.)
"""
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    sublist=[]                  #defining an empty list for adding the keys
    for i in aDict:             #defining i as the keys in aDict
        if aDict[i]== target :  #if the value equals to target, adding the key to sublist
            sublist.append(i)
    return sorted(sublist)      #return sublist woth increasing order 