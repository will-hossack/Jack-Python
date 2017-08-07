f = open("Text.txt")
f.write("This is a test")
f.close()

"""
Question: Given that Text.txt contains the single line 'Hello World!' before the program runs, what does it contain 
after?:
A. Hello World!
B. This is a test
C. Hello World!
   This is a test
D. error, program will not run
Purpose: check understanding that by default file will open in read mode and you cannot write to a file in read mode
Answer D.
"""