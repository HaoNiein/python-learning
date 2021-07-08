def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s=""                          #defining s as a empty string for adding the letter or blank 
    for i in secretWord:          #defining i as the letters in secreword
         if i in lettersGuessed : #adding i in s if i is in the letterGuessed
             s+=i
         else:
             s+="_"               #if not, adding a blank
    return s

