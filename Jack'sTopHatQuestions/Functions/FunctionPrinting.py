def square(x = 5):
    return x*x

print(square)

"""
Question: What will the above program print?:
          A. square
          B. 25
          C. error
          D. <function square at 0x10143f0d0>
Purpose: Check understanding that you can print functions directly and this returns their address in the memory, 
         this doesn't give an error, so it a possible source of bugs in your code.
Answer: D. 
"""