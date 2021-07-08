def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    slist=[]                                   #defining an empty list for adding all the numbers in tuple or list 
    for i in t:                                #defining i as the int or tuple or list in t
            if type(i)==tuple:                 #if i is tuple 
                slist += tupleTOlist(i)        #call the function of tupleTOlist to add all int in tuple to slist 
            elif type(i)==list:                #if i is list  
                slist+= listTOlist(i)          #call the function of listTOlist to add all int in list to slist
            else:                              #if i is int 
                slist.append(i)                #add the int to slist
    return (max(slist))                        #return the max number in slist 
    
def tupleTOlist(giventuple):                   #defining a function that adding the int in tuple or list to slist
    tuplelist=[]                               #defining an empty list for adding the int in tuple or list 
    for n in giventuple:                       #defining n as the element in tuple 
        if type(n)==int:                       #if n is int 
            tuplelist.append(n)                #add the int to tuplelist
        elif type(n)==tuple:                   #if n is tuple 
            tuplelist += tupleTOlist(n)        #call the function of tupleTOlist and addind the int in tuple to tuplelist
        elif type(n)==list:                    #if n is list
            tuplelist += listTOlist(n)         #call the function of listTOlist and addind the int in tuple to tuplelist
    return tuplelist                           

def listTOlist(givenlist):                    #same as tupleTOlist
    listlist=[]
    for n in givenlist:
        if type(n)==int:
            listlist.append(n)
        elif type(n)==tuple:
            listlist += tupleTOlist(n)
        elif type(n)==list:
            listlist += listTOlist(n)
    return listlist