f = open("Text.txt","r+")
print(f.read())
f.write("This is a test")
print(f.read())
f.close()

"""
Question: Given that Text.txt contains the single line 'Hello World!' before the program runs, what does the above
          program print?:
A. Hello World!
B. This is a test
C. Hello World!
   This is a test
D. Hello World!This is a test
Purpose: check understanding that reading afer writing will begin reading from where the writing finished, in this case
         it reads from the '/n' after 'This is a test' so print(f.read()) just prints a new line, and it isn't output
         by our program.
Answer A.
"""