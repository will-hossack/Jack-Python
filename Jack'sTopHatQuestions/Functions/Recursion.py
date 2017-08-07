def fcn(x):
    if x==0:
        return 0
    else:
        return x+fcn(x-1)

def main():
    print(fcn(5))

main()

"""
Question: What is the output of this program?
A. 0
B. 15
C. This program will run forever since the fcn calls itself?

Purpose: Check understanding of recursion with functions and necessity of termination condition.
Answer: B

"""
