f = open("Text.txt","w")
f.write("This is a test")
f.close()

"""
Question: Given that Text.txt contains the single line 'Hello World!' before the program runs, what does it contain 
after?:
A. Hello World!
B. This is a test
C. Hello World!
   This is a test
Purpose: check understanding that what you write to a file will write over the top of its current contents
Answer B.
"""