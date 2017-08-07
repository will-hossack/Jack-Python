"""
short program demonstrating how to implement max and min functions

"""

import random # we will use random to test our functions at the end in the main method

def max(x,y):
    if x>=y:
        return x
    else:
        return y

def min(x,y):
    if x<=y:
        return x
    else:
        return y

def main(): # lets generate 5 pairs of random numbers, compare them and print the result to the command line
    for i in range(0,5):
        x = random.randint(0,1000)
        y = random.randint(0,1000)
        print(str(max(x,y))+" is the maximum of "+str(x) + " and "+ str(y))
        print(str(min(x,y)) + " is the minimum of " + str(x) + " and " + str(y)+"\n")


main()