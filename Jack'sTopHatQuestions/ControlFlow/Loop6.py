numbers = [0,1,2,3,4]
for i in numbers:
    numbers.append(i)
    print(numbers)

"""
Question: What is the ouput of this program?:
A. [0,1,2,3,4,0,1,2,3,4]
B. [0,1,2,3,4]
C. error
Purpose: Check understanding that for loop iterating over a sequence does not make a copy. Here we keep appending 
         elements of the list to the end of the list, so we never actually finish iterating through the list.
Answer: C. 

"""