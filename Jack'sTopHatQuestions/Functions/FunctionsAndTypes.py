def max(x,y):
    if(x>y):
        return x
    else:
        return y

print(max(1+1j,2+2j))

"""
Question: What is the output of the above code?:
          A. 2+2j
          B. 2
          C. error
Purpose:  Check awareness that functions in Python will accept any type, and it is the job of the programmer 
          either to implement the function such that it deals with all possible inputs, or make sure they only call the
          function on the correct types.
Answer:   C.
"""
