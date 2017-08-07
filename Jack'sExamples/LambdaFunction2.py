"""
Another use of lambda functions is returning a function from another function.
"""

def transform(n):
    # here we return a lambda function with parameter n from the transform function
    return lambda x: x + n

def add(x,y):
    return x+y
def transform2(n):
    return add(n)

def main():
    # we create an instance of our lambda function by initializing f with transform(3)
    f = transform(3)
    # here we call our lambda function to act on the int 4 and then print the outcome
    print(f(4))
main()

"""
note that something like: 
def add(x,y):
    return x+y
    
def transform2(n):
    return add(n)
    
with normal functions would not work since add needs to take two arguments. so in this case lambda functions are 
necessary.
"""