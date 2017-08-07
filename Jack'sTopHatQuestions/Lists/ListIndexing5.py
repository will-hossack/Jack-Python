def main():
    list = [1,2,3,4,5]
    print(list[4:42])
main()

"""
What is the output of the program?:
A. [4,5]
B. [5]
C. error, second index is out of bounds.
Purpose: Check understanding of range slice indexing, that one of the bounds may be out of range but still be handed 
         gracefully.
Answer: B.
"""