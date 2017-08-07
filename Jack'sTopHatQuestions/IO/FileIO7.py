f = open("Text.txt","wb")
f.write("This is a test")
f.close()

"""
Question: Given that Text.txt contains the single line 'Hello World!', what will it contain after the program has
          run?:
A. Hello World!
B. Hello World!This is a test
C. This is a test
D. Hello World!
   This is a test
E. error
Purpose: Check understanding that files can be opened in binary mode, for reading and writing binary data, and that you 
         cannot write str objects to a binary file
Answer: E
"""
