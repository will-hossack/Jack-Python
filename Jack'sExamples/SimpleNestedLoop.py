"""
Nested loops are very common in programming, this is where we have a loop inside another loop.
In this simple program we will use nested loops to print out the times tables.

"""

def main():
    # Note how we need different indices for each loop.
    for i in range (1,13):
        for j in range (1,13):
            # using end =" " prints a " " space at the end of the print statement rather than a "\n" newline
            print(str(i*j),end=" ")
        # we have blank print here just to get a new line so it is formatted nicely in the terminal window
        print()
main()