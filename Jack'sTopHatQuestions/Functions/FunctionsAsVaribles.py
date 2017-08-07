def add(x,y):
    return x+y

myAdd = add
print(myAdd(1,2))

"""
Question: What is the output of the program?: 
          A. 3
          B. myAdd(1,2)
          C. error
Purpose:  Check understanding that functions can be treated like variables in Python (like function pointers in C)
Answer :  A.
"""