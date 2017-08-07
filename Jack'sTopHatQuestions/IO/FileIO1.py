f = open('Text.txt','w')
print(f.read())
f.close()

"""
Question: Given that Text.txt contains a single line 'Hello World! what will the output of the program be?:
A. Hello World!
B. (Nothing)
C. error
Purpose: Check understanding that files must be opened as either to write to or read from and you cannot read from a 
write file
Answer: C.
"""