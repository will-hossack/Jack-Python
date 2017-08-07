f = open("Text.txt","r+")
f.write("This is a test")
f.close()

"""
Question: Given that Text.txt contains the single line 'Hello World!' before the program runs, what does it contain 
after?:
A. Hello World!
B. This is a test
C. Hello World!
   This is a test
D. Hello World!This is a test
Purpose: check understanding that if you open a file in r+ mode you can read and write, and that it will append and not
         overwrite the file.
Answer D.
"""