from words import wordsList
import random
import time

def intro():
    print("Let's play hangman")
    time.sleep(1)
    print("We will begin the game in a few seconds")
    time.sleep(1)
    print("Enjoy!")
    time.sleep(1)
    print("Initializing")
    time.sleep(1)
    print("Choosing a word")
    time.sleep(3)
    print(chr(27) + "[2J") 

hangmanStage = ["""
                +------------
                |           |
                            |
                            |
                            |
                            |
                            |
                            |
                    +---------------+""","""
                +------------
                |           |
                O           |
                            |
                            |
                            |
                            |
                            |
                    +---------------+""","""
                +------------
                |           |
                O           |
                |           |
                            |
                            |
                            |
                            |
                    +---------------+""","""
                +------------
                |           |
                O           |
               \|           |
                            |
                            |
                            |
                            |
                    +---------------+""","""
                +------------
                |           |
                0           |
               \|/          |
                |           |
                            |
                            |
                            |
                    +---------------+""","""
                +------------
                |           |
                0           |
               \|/          |
                |           |
                            |
                            |
                            |
                    +---------------+""","""
                +------------
                |           |
                0           |
               \|/          |
                |           |
               /            |
                            |
                            |
                    +---------------+""","""
                +------------
                |           |
                0           |
               \|/          |
                |           |
               / \          |
                            |
                            |
                    +---------------+"""]
def play(word):
    toBeGuessed = "_"*len(word)
    guessed = False
    wordList = list(word)
    lifePoints = 7
    lettersGuessed = []
    wordsGuessed = []
    time.sleep(2)
    while not guessed and lifePoints > 0:
        print(chr(27) + "[2J")
        print("You have "+ str(lifePoints) +" guess remaining.")
        print(hangmanStage[7-lifePoints])
        print("")
        print(toBeGuessed) 
        print("")  
        guess = input("Please enter your guess - letter or the word: ").upper()
        if guess.isalpha() and len(guess) == 1:
            if guess in lettersGuessed:
                print("You already provided the letter. Guess again")
            elif guess not in wordList:
                print("Your letter guess is not in the word")
                lifePoints -= 1
                lettersGuessed.append(guess)
            else:
                print("You have a correct letter guess")
                lettersGuessed.append(guess)
                tobeGuessed_list = list(toBeGuessed)
                position = [i for i, letter in enumerate(word) if letter == guess]
                for index in position:
                    tobeGuessed_list[index] = guess
                toBeGuessed = "".join(tobeGuessed_list)   
                if "_" not in toBeGuessed:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in wordsGuessed:
                print("Already tried the word")
            elif guess != word:
                lifePoints -= 1
                wordsGuessed.append(guess)
            else:
                guessed = True
                toBeGuessed = word
        else:
            print("Not a valid guess!")
        time.sleep(1)
    if guessed:
        print(chr(27) + "[2J")
        print("The word is "+word)
        print("")
        print("Congratulations you win!")
        print("")
        time.sleep(3)
        
    else:
        print(chr(27) + "[2J")
        print(hangmanStage[7])
        print("")
        print("You lost. Sorry. Better luck next time")
        print("")
        print("The word is "+word)
        print("")
        time.sleep(3)
    
print(chr(27) + "[2J") 
intro()
word = random.choice(wordsList).upper()
play(word)
while str(input("Do you still want to play? Y for yes/other key to terminate \n").upper()) == "Y":
    word = random.choice(wordsList).upper()
    play(word)

