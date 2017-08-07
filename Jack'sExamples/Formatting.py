"""
Example of printing using .format()
"""

# Imagine we has writeen a game which ouput a player score
playerScore = 123
totalScore  = 1274

percentage = float(playerScore)/totalScore*100

# using indices this can be printed as
print("player score: {0:4d}, out of {1:4d}. ({2:3.1f}%)".format(playerScore,totalScore,percentage))




