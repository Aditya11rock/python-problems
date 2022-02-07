import random
import time
fruit=["apple","pear","banana","mango","watermelon","grapes","papaya","cherry","orange","pineapple",
     "strawberry","pomogranate"]
marvel_heros=["captain america","thor","ant man","iron man","hulk","doctor strange","black panther",
              "spider man","hawkie","natasha","war machine","jarvis","vulkerie","edith","loki",
              "thanos","rocket","gamora","star lord","groot","tony stark"]

userGuessList=[]
userGuesses=[]
playGame=True
category=""
continueGame="Y"
secretWord=''

name=input("Enter your Name: ")
print("hello ",name.capitalize()," Let's start playing Hangman!! ")
time.sleep(2)
print("the objective of the game is to guess the secret word chosen by the computer.")
time.sleep(2)
print("you can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
time.sleep(3)
print("let the fun begin!")
time.sleep(1)

#choosing random word from the desired catagory
while True:
    while True:
        if category.upper()=='F':
            secretWord=random.choice(fruit)
            break
        elif category.upper()=='M':
            secretWord=random.choice(marvel_heros)
            break
        else:
            category=input("Please select a valid category: F for fruits / M for marvel heroes;"
                           "X to exit")

        if category.upper()=="X":
            print("Bye. See you next time!")
            playGame=False
            break

    if playGame:
        secretWordList=list(secretWord)
        attempts=len(secretWord) + 2

#Utility function to print User Guess List
        def printGuessedLetter():
            print("your secret word is: " + ''.join(userGuessList))

        userGuessList=[]
        for i in secretWordList:
            userGuessList.append('_')

        printGuessedLetter()
        print("the number of allowed guesses for this word is: ", attempts)

#function to print userguesslist

#starting the game
        while True:
            print("Guess a letter: ")
            letter=input()
            if letter in userGuesses:
                print("You have already guessed this letter, try something else.")
            else:
                attempts -=1

                userGuesses.append(letter)
                if letter in secretWordList:
                    print("Nice guess!")
                    if attempts >0:
                        print("you have ",attempts," guess left")
                    for i in range(len(secretWordList)):
                        if letter==secretWordList[i]:
                            letterIndex=i
                            userGuessList[letterIndex]=letter.upper()
                            printGuessedLetter()
                else:
                    print("Oops! Try again.")
                    if attempts >0:
                        print("you have ",attempts," guess left")
                        printGuessedLetter()
#win/loss logic

            joinedList=''.join(userGuessList)

            if joinedList.upper()==secretWord.upper():
                print("yay!! you won.")
                break
            elif attempts==0:
                print("Too many Guesses!, Sorry better luck next time.")
                print("The secret word was: "+ secretWord.upper())
                break

#Play again logic for the game
        continueGame=input("Do you want to play again? Y to continue, any other key to quit")

        if continueGame.upper()=='Y':
            category=input("Plese select a category: F for fruits / M for Marvel-heroes")
            userGuessList=[]
            userGuesses=[]
            playGame=True

        else:
            print("thank you for playing. See you next time!")
            break







