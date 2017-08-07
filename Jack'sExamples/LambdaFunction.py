"""
Short program to illustrate the use of lambda functions. Lambda functions are useful when you need a function in
your code to perform some task, but you only need it once, instead of defining an entire function, you can define a
lambda function inline to simplify your code.
"""

def main():
    # filter creates a list of elements for which the function in its first argument returns true. We could have
    # written a normal function to replace the lambda function, but this might be the only place in our program we
    # need to call a function that returns true for multiples of 5, so its best to use a lambda function here.
    mult5 = list(filter(lambda x: x % 5 == 0,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(mult5)

main()