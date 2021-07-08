def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
     s = list(string.ascii_lowercase)  #makeing all the letter become a list  
    emptyS=""                          #defining a empty string for adding letters not in the letterDuessed
    for i in s :
        if i not in lettersGuessed:    
            emptyS += i
    return emptyS
    
    
