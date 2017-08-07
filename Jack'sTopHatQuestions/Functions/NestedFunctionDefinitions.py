def fcn1():
    def fcn2():
        return 2
    return 1

"""
Question: What is the correct way to call fcn2?:
          A. fcn2()
          B. fcn1.fcn2()
          C. fcn1().fcn2()
          D. you cannot call a function that is defined in another function 
Purpose:  Check understanding that you cannot call functions defined in other functions
Answer:   D.
"""
