def myFcn(*args):
    for arg in args:
        print(arg,end=' ')

myFcn(1,"Hello World",True, 3.14)

"""
Question what is the output of the program?:
A. 1
B. 1 Hello World True 3.14
C. error
Purpose: Check understanding that by using *args parameter you can pass the function a series of arguments that it
         will then access as a sequence
Answer: C. 
"""