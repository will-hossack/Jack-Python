def squareList(list):
    for i in range(0,len(list)):
        list[i]=list[i]*list[i]
def square(value):
    value = value*value

def main():
    myList = [1,2,3,4,5,6,7,8,9]
    print(str(myList))

    myValue = 4
    print(myValue)

    squareList(myList)
    print(myList)

    square(myValue)
    print(myValue)

main()

"""
Question: What will this program print?

A. [1, 2, 3, 4, 5, 6, 7, 8, 9]
   4 
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   4
   
B. [1, 2, 3, 4, 5, 6, 7, 8, 9]
   4
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   16
   
C. [1, 2, 3, 4, 5, 6, 7, 8, 9]
   4
   [1, 4, 9, 16, 25, 36, 49, 64, 81]
   4
   
D. [1, 2, 3, 4, 5, 6, 7, 8, 9]
   4
   [1, 4, 9, 16, 25, 36, 49, 64, 81]
   16
   
Purpose: to check understanding of passing a list vs. passing other fundamental data types to a function that changes
that variable in some way. Lists get changed by function, other data types do not.

Correct Answer C.

"""