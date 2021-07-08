def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in list(secretWord):         #defining i as the letters in secreword, and make secreword become a list 
        if i not in lettersGuessed :   #if the letter is not in the letterGuessed, return false
            return False
    return True
    
