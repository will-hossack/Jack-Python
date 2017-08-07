def myFcn(normalArgument, *args, **kwargs):
    print(normalArgument)
    for arg in args:
        print(arg,end=' ')
    print()

    for kw in kwargs:
        print(kw,":",kwargs[kw])

myFcn("1st argument","args1",kw1="kwarg1",)

"""
Question: What is the output of the program?:
A. 1st argument
B. 1st argument
   args1 
   kw1 : kwarg1
C. error
Purposes: Check understanding that you can have a mix of normal arguments, *args arguments and **keyword arguments
Answer: B.
"""