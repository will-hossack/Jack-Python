def fcn1():
    def fcn2():
        print("Hello")
    return fcn2

"""
Question: What is the correct way to call fcn2?:
          A. innerFcn = fcn1()
             innerFcn()
          B. fcn1()()
          C. It can't be done
Purpose: Check understanding that one may return functions without the (), this returns the function as a varible, 
         ready to use by just applying the ()
Answers: A,B.
"""
