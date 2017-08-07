globalVar = 0

def setGlobal1():
    global globalVar
    globalVar =1

def setGlobal2():
    globalVar =2

def printGlobalVar():
    print(globalVar)

setGlobal1()
printGlobalVar()

setGlobal2()
printGlobalVar()

"""
Question: What does this program print?:
          A. 1
             2
          B. 1
             1
          C. 2
             2
          D. 2
             1
Purpose: Check understanding that global variables need to be accessed through global specifier if you want to access
         them
Answer:  B.
"""
