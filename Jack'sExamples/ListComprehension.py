"""Shor piece of code to demonstrate using nested list comprehension to take the tranpose of a 3x4 matrix"""

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(matrix)
transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)

# Note that this is equivalent to
transpose = []
for i in range(4):
    transpose.append([row[i] for row in matrix])

# which uses list comprehension once, and one for loop

# which is in turn equivalent to
transpose = []
for i in range (4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transpose.append(transposed_row)

# which uses no list comprehension and two for loops
