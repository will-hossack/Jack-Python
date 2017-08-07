f = open("Text.txt", "r")
for i in f:
    print(i)
f.close()

"""
Question: Given that Text.txt contains the lines: Hello world!
                                                 How are you?
                                                 
          What is the output of the above program?:
A. Hello
   World!
   How
   are
   you?
B. Hello world!
   How are you?
C. Hello world!
   
   How are You?
   
Purpose: check understanding that f can be iterated over and will return the lines from the file, and that the lines 
         themselves contain '\n' new line characters.
Answer: C.
"""