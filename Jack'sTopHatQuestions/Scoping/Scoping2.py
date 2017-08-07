x = 5
def fcn1():
    x = 6
    def fcn2():
        print(x)
    fcn2()

def fcn3():
    def fcn2():
        print(x)
    fcn2()

fcn1()
fcn3()

"""
Question: What is the output of the above program?:
          A. 6
             5
          B. 6
             6
          C. 5
             6
          D. 5
             5
Purpose:  Check understanding of scoping and namespaces.
Answer :  A.
          """