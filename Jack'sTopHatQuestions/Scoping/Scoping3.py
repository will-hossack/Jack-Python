i = 5

def myFcn(x = i):
    return x*x
i = 6

print(myFcn())

"""
Question: What is the output of the program?:
A. 25
B. 36
C. error
Purpose: Check understanding that default values are evaluated at the point of function definition in the defining
         scope.
Answer: A.
"""