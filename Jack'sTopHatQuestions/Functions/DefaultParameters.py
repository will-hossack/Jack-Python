def fcn(x=5):
    return x

def main():
    print(str(fcn()))
    print(str(fcn(2)))
    print(str(fcn(5)))


main()

"""
Question: what is the output of this program?
A. 5
   2 
   5
   
B. 5
   5 
   5 
   
C. 0
   2     
   5
   
Purpose: to check understanding of default parameters and what happens when you do and don't supply an argument.
Correct Answer: A
    
"""