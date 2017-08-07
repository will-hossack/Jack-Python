def myFcn(x):
    if x>5:
        print(str(x)+ " is greater than 5")
        return
    if x>3:
        print(str(x)+" is greater than 3")
        return
    if x>1:
        print(str(x)+ " is greater than 1")
        return

myFcn(4)

"""
Question: What is the output of this program?:
A. 4 is greater than 3
B. 4 is greater than 3
   4 is greater than 1
C. error
Purpose: Check understanding that if statements can be used to have custom functionality depending on the function 
         argument, and that return stops the execution of the function at the line it is written an returns to the 
         function caller. 
Answer: A. 
 """

