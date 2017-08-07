"""
Example Program to print numbers 1 - 100 in a nice formatted way. Demonstrates use of conditionals, loop and %
operator
"""

def main():
    # we want to print numbers from 1 to 100 which means we need 101 as the maximum in our range
    for i in range (1,101):
        # if the number we are printing is less than 10 prefix it with 0 for formatting purposes
        if(i<10):
            # end="" ensures we dont have a new line after we print out zero, we just get an empty string
            print(0,end="")
            # end= " " prints a space at the end of the line inestead of a "\n" newline
        print(i,end=" ")
        # if we reach a multiple of ten, which we check with the modulo operator, print a newline so it is nicely
        # formatted
        if i%10==0:
            print()
main()