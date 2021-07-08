def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", str(len(secretWord)),"letters long.")                          #user inputs letter
    print ("------------")
    guess = 8                                                                                               #guessing 8 times 
    lettersGuessed =""                                                                                      #defining a empty string for adding user's input
    while guess > 0:                                                                                        #befor 8 times running out, following program will be continued 
        print("You have",str(guess),"guesses left.")
        print ("Available Letters:", getAvailableLetters(lettersGuessed))
        lettersGuessedinput = input("Please guess a letter:")                                               #user's input

        if lettersGuessedinput in secretWord and lettersGuessedinput in \                                   #if user's input is in secretWord and in AvailableLetters,   
            getAvailableLetters(lettersGuessed):                                                            
            lettersGuessed += lettersGuessedinput                                                           #1)adding this letter in lettersGuessed
            print ("Good guess:", getGuessedWord(secretWord, lettersGuessed))                               #2)print good guess and call the function of getGuessedWord
            print ("------------")
        elif lettersGuessedinput not in secretWord and lettersGuessedinput in \                             #if user's input isn't in secretWord but still in AvailableLetters
            getAvailableLetters(lettersGuessed):
            lettersGuessed += lettersGuessedinput                                                           #1)adding this letter in lettersGuessed
            print ("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))      #2)print xxxx and call the function of getGuessedWord
            guess -= 1                                                                                      #3)chance of guessing -1 
            print ("------------") 
        elif lettersGuessedinput not in getAvailableLetters(lettersGuessed):                                #if user's input is in secretWord but not in AvailableLetters ((letter has already been guessed   
            print ("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))  #1)print xxxx and call the function of getGuessedWord
            print ("------------")
   
   
        if getGuessedWord(secretWord, lettersGuessed) == secretWord:
            print ("Congratulations, you won!")
            break
    else:
        print ("Sorry, you ran out of guesses. The word was else.")

