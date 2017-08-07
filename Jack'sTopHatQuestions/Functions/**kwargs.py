def myFcn(**kwargs):
    for kw in kwargs:
        print(kw, ":", kwargs[kw])

myFcn(name = "John Smith ", DOB = "01/01/1900", Occupation = "student")

"""
Question: What is the output of the program?:
A. John Smith
B. name : John Smith 
   DOB : 01/01/1900
   Occupation : student
C. error
Purpose: Check understanding that functions can take kw arguments in the form of key = data, and that the key and the 
         data can be used in the function
Answer: C.
"""