"""
This program uses Nested loops to print out fancy triangles of numbers

First function prints: 1
                       1 2
                       1 2 3
                       1 2 3 4
                       1 2 3 4 5

Second function prints: 5 4 3 2 1
                        4 3 2 1
                        3 2 1
                        2 1
                        1

Third function prints:          1
                              2 1
                            3 2 1
                          4 3 2 1
                        5 4 3 2 1
"""

# Function to print the first style of triangle
def printTriangleOne():
    outer = 1
    while outer <= 5:
        inner = 1
        while inner <= outer:
            print(inner, end=" ")
            inner += 1
        print()
        outer += 1

# Function to print the second style of triangle
def printTriangleTwo():
    outer = 5
    while outer>=1:
        inner = outer
        while inner>=1:
            print(inner,end=" ")
            inner-=1
        print()
        outer-=1

# Function to print the third style of triangle

def printTriangleThree():
    outer = 1
    while outer<=5:
        inner = 5
        while inner >= 1:
            if inner<=outer:
                print(inner,end=" ")
            else:
                print(end="  ")
            inner-=1
        print()
        outer+=1



# Main function to call the triangle printing functions
def main():

    # Call the first function
    printTriangleOne()
    # Separate second call with some empty lines
    print("\n")
    printTriangleTwo()
    # Separate third call with some empty lines
    print("\n")
    printTriangleThree()

main()

