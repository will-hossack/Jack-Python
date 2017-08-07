"""
This more complicated guessing game makes further use of user interaction as well as functions to deal with the game
logic that improve the modularity of the code
"""
import random

def playGame(): # function to handel the game logic and return a bool representing the outcome
    answer = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100 (inclusive) you have 10 guesses to get it right!")

    for guess in range(0,10):
        # get the guess, using the for index to output the #guess
        userGuess = int(input("Guess #"+str(guess+1)+": "))
        # three possible guesses
        if(userGuess<answer):
            print("Too small! Try again!")
        elif(userGuess>answer):
            print("Too big! Try again!")
        else:
            # case that player has won
            return True
    # otherwise player has lost
    return False

# friendly main function to play the game with the user
def main():
    # get the players name for use in the output
    name = str(input("please enter your name: "))
    #ask the user whether they want to play, if they do we may use our playGame() function, otherwise exit
    userInput = str(input("Hello "+name+" would you like to play a game?(y/n): "))

    while userInput=="y":
        # since our function returns a bool we can directly use it in our conditional statement, since everytime
        # our if statement is reached, the playGame() function will be executed.
        if(playGame()):
            print("congratulations "+name+" you have won!")
        else:
            print("oh no! you lost")
        # update whether the user wants to play again or not
        userInput=str(input("Would you like to play again?(y/n):"))
main()




