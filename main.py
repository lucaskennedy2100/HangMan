from wonderwords import RandomWord
r = RandomWord()
man = 0 #counter for score
wordList = [] #list of chars in word
guessed = [] #list of guessed chars

def startGame():
    global man
    #zero everything
    man = 0
    wordList.clear()
    guessed.clear()
    #begin generating word
    word = r.word() #generate word
    i = 0
    for char in word: #fill wordlist
        wordList.append(char)
        i = i+1

    printMan()
        

def printMan():
    print("           ____")
    print("          |    |")
    #first point
    if man >= 1:
        print("          O    |")
    else:
        print("               |")
    #second-fourth points
    if man == 2:
        print("         -     |")
    if man == 3:
        print("         -|    |")
    if man >= 4:
        print("         -|-   |")
    if man < 2:
        print("               |")
    #fifth and sixth points
    if man == 5:
        print("         |     |")
    if man >= 6:
        print("         | |   |")
        gameOver() #game over
    if man < 5:
        print("               |")

    #print guessed letters
    print("Guessed letters: ", end = "")
    for item in guessed:
        print (item, end=" ")
    print()

    correctAns = []
    #print the key
    for item in wordList:
        found = False
        for guess in guessed:
            if item == guess:
                found = True
        if found:
            correctAns.append(item)
            print(item, end = " ")
        else:
            print("_", end = " ")
    
    if correctAns == wordList: #check if they've won
        winner()

    getInput()


def winner():
    #game over
    print("\nYOU WIN!\n")
    print("The answer is: ")
    for item in wordList:
        print(item, end = "")
    #end program
    userInput = input("\nPress '-' to play again.")
    if userInput == "-":
        startGame()
    exit()

def gameOver():
    #game over
    print("\nGAME OVER\n")
    print("The answer was: ")
    for item in wordList:
        print(item, end = "")
    #end program
    userInput = input("\nPress '-' to play again.")
    if userInput == "-":
        startGame()
    exit()

def getInput():#get input
    global man
    userInput = input("\nGuess a letter or the word(Note: guessing the word wrong will result in instant loss): ")
    #check for guessed words
    if len(userInput) > 1:
        found = True
        i = 0
        for char in userInput:
            if char != wordList[i]:
                found = False
            i+=1
        if found:
            winner()
        gameOver()
        

    for item in guessed:#if they already guessed something, let them go again
        if userInput == item:
            print("You already guessed ", item, "Guess again: ")
            getInput()
    found = False
    for item in wordList:
        if userInput == item:
            found = True
    guessed.append(userInput)
    if not found:
        man+=1
    printMan()#start new turn


#start
print("Welcome to Hangman!")
startGame()


#access list of words?
#pick one and draw out soaces
#ask for inoput

#           ____
#          |    |
#          O    |
#         -|-   |
#         | |   |
#               |