"""
Simple program to demonstrate how to swap values in python
"""
from timeit import Timer
# In other programming languages one would implement a swap function using a temporary value as follows

a = 1
b = 2
print("a = " + str(a)+", b = " + str(b))
print("swapping...")
temp = a
a = b
b = temp
print("a = " + str(a)+", b = " + str(b)+"\n")

# However in Python we can implement tuples to do the same thing, (this is an example of being "pythonic")

a, b = 1, 2
print("a = " + str(a)+", b = " + str(b))
print("swapping...")
a, b = b, a
print("a = " + str(a)+", b = " + str(b) + '\n')

# in fact it is more efficient to use the tuple method as the following code demonstrates, (values will vary from
# machine to machine)

print("1st method takes: " + str(Timer('t=a; a=b;b=t','a=1; b=2').timeit()) + " seconds")
print("2nd method takes: " + str(Timer('a, b = b, a', 'a=1; b=2').timeit()) + " seconds")


