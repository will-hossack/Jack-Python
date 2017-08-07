import math

print(math.fmod(-1e-100,1e100))
print(-1e-100%1e100)

"""
Question: What is the output of the above code?:
          A. -1e-100
             1e+100
          B. -1e-100
             -1e-100
          C.  1e+100
             -1e-100
          D.  1e+100
              1e+100
Purpose: Check understanding that some operators such as % have precession errors, and that modules such as math provide
         alternate functions as solutions. 
         math.fmod(x,y) is exactly equal to x - n*y for some integer n, such that the result has the same sign as x and 
         magnitude less than abs(y). x%y returns a result with sign of y instead. In the above -1e-100%1e100 is 
         1e100-1e-100 which cannot be represented exactly as a float and rounds to 1e100.
Answer:  A.
"""