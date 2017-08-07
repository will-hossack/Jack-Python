f = open("Text.txt","a")
f.write("J")
f.close()

"""
Question: Given that Text.txt contains the single line 'Hello World!', what will it contain after the program has
          run?:
A. Hello World!
B. Jello World!
C. Hello World!J
Purpose: Check understanding that files can be opened in append mode and that the new content will be added directly
         onto the end of the current text in the file.
Answer: C
"""
