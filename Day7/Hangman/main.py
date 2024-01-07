import random

from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages
print(logo)

chosen_word = random.choice(word_list).upper()
word_length = len(chosen_word)

end_of_game = False
guesses = []
gameOver = False
def printLetters(word, guess_input):
    print("YouveGuessed: "+ str(guess_input))
    for i in range(len(str(word))):

        if(word[i] in guess_input):
            print(word[i],end=' ')
        else:
            print("_",end=' ')
    print("\n")

def checkGuesses(guess, guesses):
    if(guess not in guesses):
        return True
    else:
       return False

def isGameOver(word,guess_input,stages):
    strikes = 1
    successFlag = True
    for i in range(len(str(word))):
        if(word[i] not in guess_input):
            successFlag = False
    for i in range(len(guess_input)):
        if(guess_input[i] not in word):
            strikes = strikes + 1
    if(strikes ==8):
        print(str(stages[int(-1*(strikes-1))]))
        print("Game Over - You Lost")
        print("The Word Was " + str(word))
        return True
    if(successFlag == True):
        print("Congrats You Won!")
        return True
    else:
        print("Please Keep Going")
        print("Stike: " + str(strikes-1) +"/7")
        print(str(stages[int(-1*(strikes-1))]))
        return False
            
printLetters(chosen_word,' ')

def collectInput(guesses):
    uniqueGuess = False
    activeguess = input("Please Guess a Letter: ").upper()
    while activeguess.isalpha() == False or uniqueGuess == False:
        if(activeguess.isalpha()== False):            
            print("You've previously Guessed: " + str(guesses))
            activeguess = input("Please Guess a Letter not number... dumbie : ").upper()
            print("test:" + str(checkGuesses(activeguess,guesses)))
        
        if(checkGuesses(activeguess,guesses) == False):
            activeguess = input("Please Guess a UNIQUE Letter not number... dumbie : ").upper()
        else:
            guesses.append(str(activeguess))
            uniqueGuess = True
    return(guesses)


#Run the Game
while(gameOver == False):
    guesses = collectInput(guesses)
    printLetters(chosen_word,guesses)
    gameOver = isGameOver(chosen_word,guesses,stages)
    


    
