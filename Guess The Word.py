#5/11/2018
import random


def chooseWord():
    wordList = ["hello", "day", "alphabet", "collage", "germany", "war", "black hole", "earth", "xenophobia", "soup"]

    chosenWord = wordList[random.randrange(len(wordList))]

    return chosenWord


def letterInWord(letter, word, coolList):
     if letter in word:

        for i in range(len(word)):

            if word[i] == letter:
                coolList[i] = word[i]
     return coolList


count = 0
gameWord = chooseWord()
maxGuess = len(gameWord) + 3
gameList = ["*"] * len(gameWord)
print("Welcome to the Word Guessing Game!")
while count < maxGuess:
    print("You have " + str(maxGuess) + " guesses left!")
    userInput = str(input("Choose your letter!: "))
    print(letterInWord(userInput, gameWord, gameList))
    maxGuess -= 1

    if "*" in gameList:
        continue
    else:
        print("Congrats! You won!")
        break




