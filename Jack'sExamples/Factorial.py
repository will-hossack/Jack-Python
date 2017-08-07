"""
Recursive function to calculate n!=n*n-1*...*2*1
"""

def factorial(n):
    # termination condition
    if n == 0:
        # using that 0! = 1
        return 1
    else:
        # this is where the recursion happens
        return n*factorial(n-1)

# main method to check our factorial function works for first 5 integers
def main():
    # first 6 factorial numbers (staring from 0), these can be easily calculated by hand
    factorialNumbers = [1,1,2,6,24,120]
    # boolean value to tell us whether the function works
    functionWorks = True
    # let's check that our function works for first 5 integers
    for i in range(0,6):
        if(factorial(i)!=factorialNumbers[i]):
            # print the term which the function breaks on
            print(str(i)+"! is wrong")
            # if its broken we must set our boolean to false since the default is true
            functionWorks = False
            # stop the loop, we know the function is broken at this point
            break
    # print out whether the function worked or not
    if(functionWorks):
        print("Factorial function is correct!")
    else:
        print("Factorial function is incorrect!")

main()


