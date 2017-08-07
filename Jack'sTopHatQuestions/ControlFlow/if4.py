def doSomething():
    print("done something")

def doNothing():
    print("done nothing")

if "":
    doNothing()
if " ":
    doSomething()

"""
Question: What is the output of the program?:
A. done something
B. done nothing
C. (nothing)
D. error
Purpose: Check understanding that empty strings are considered False, and that even though " " is just a space, is is 
         still non-empty and hence True
Answer: A
"""