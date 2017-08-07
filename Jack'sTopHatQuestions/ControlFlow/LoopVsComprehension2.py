list1 = []
for i in [1,2,3]:
    for j in [3,1,4]:
        if i==j:
            list1.append((i,j))

list2 = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]

"""
Question: What is the value of list1==list2?:
          A. True
          B. False
          C. (==) operation not defined on lists
Purpose:  Check understanding that list comprehension can be used to efficiently perform list operations. 
Answer :  B.
"""