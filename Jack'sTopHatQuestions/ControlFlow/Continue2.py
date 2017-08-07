count = 0
while count<10:

    if count%2==0:
        continue
    print(count,end=' ')
    count += 1

"""
Question: What is the output of the above program?
A. 1 3 5 7 9 
B. 0 1 2 3 4 5 6 7 8 9
C. error
Purpose: Check understanding of the continue keyword and its effects. Here by jumping to the start of the loop
         on all even terms we miss the increment and count forever remains at 0
Answer C. 
"""
