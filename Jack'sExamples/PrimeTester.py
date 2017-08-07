"""
Function to test whether or not a given number is prime.

An integer n is said to be prime if its only divisors are 1 and n, and n is not 1.

This program uses a very simple trial division test. We are essentially checking whether any integer between 1 and n
divides n, if it does we know the number is not prime. This is by no means optimal, but a good place to start.

One simple optimisation is to note that we don't need to check all integers between 1 and n, only integers up to (and
including sqrt(n) since if k>sqrt(n) and k divides n then n/k < sqrt(n) is an integer, so we would have already found
it).

This algorithm will not work well for large integers, try it!
"""

def isPrime(n):
    i = 2 #
    if(n==1): ## We have to deal with n=1 case seperately since our algorithm won't deal with it.
        return False
    while(i*i<=n): ## Check all integers less than square root of n
        if(n%i==0): ## Use mod operator to check whether i divides n
            return False ## if i divides n we may return false, the function will end here
        i+=1 ## otherwise increment i and carry on
    return True ## if after checking all integers we have no divisors n is prime

def main(): ## main method to check our program works for first 20 numbers
    for i in range(1,21):
        if(isPrime(i)): ## since our function returns a bool we can use it in the conditional statement without comparison
            print(str(i)+ " is prime.")
        else:
            print(str(i) + " is not prime")

main()


