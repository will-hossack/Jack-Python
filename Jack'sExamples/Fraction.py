"""
class to implement a fraction object of the form x/y where x and y are integers. Numerator and denominator are held as
two member varibled "numerator" and "denominator"
"""


class Fraction(object):
    # constructor to take two arguments representing the numerator and denominator, assume default argument for
    # denominator is 1, that way if only one argument is supplied the object will just be a fraction representation of
    # an integer
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        # reduce fraction to simplest form using the reduce() method below
        self.reduce()

    # by making the method static we can call it without having the create an instance of fraction in main
    # this gcd() method will be used to reduce the fraction to its simplest form
    @staticmethod
    def gcd(x, y):

        if y == 0:
            return x
        else:
            return Fraction.gcd(y, x % y)

    # method to reduce the fraction into its simplest form, we wont need to call this method in our main program since
    # it is called in the constructor, so Fraction objects will always be in their simplest form
    def reduce(self):
        gcd = Fraction.gcd(self.numerator, self.denominator)
        self.numerator /= gcd
        self.denominator /= gcd



    # (*) operator overload with Fraction instance as left argument, this can take either another fraction as it's
    # right argument or an integer
    def __mul__(self, other):
        # if the right argument is a Fraction implement multiplication of two fractions as a/b * c/d = a*c/b*d and
        # reduce the fraction down
        if(isinstance(other,Fraction)):
            # we implement the multiplication of two fractions and reduce it by calling the Fraction constructor to
            # return a reduced fraction
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        # if the right argument is an int implement multiplaction of a fraction by an integer as a/b * c = ac/b and
        # reduce the fraction
        if(isinstance(other,int)):
            # multiply numerator by integer, then call constructor with original denominator in order to return
            # fraction that has been reduced to it simplest form.
            return Fraction(self.numerator*other,self.denominator)

    # (*) operator with Fraction instance as right argument, this can take either another fraction as it's left argument
    # or an integer
    def __rmul__(self, other):
        # if the left argument is a Fraction implement multiplication of two fractions as a/b * c/d = a*c/b*d and
        # reduce the fraction down
        if (isinstance(other, Fraction)):
            # we implement the multiplication of two fractions and reduce it by calling the Fraction constructor to
            # return a reduced fraction
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        # if the left argument is an int implement multiplaction of a fraction by an integer as a/b * c = ac/b and
        # reduce the fraction
        if (isinstance(other, int)):
            # multiply numerator by integer, then call constructor with original denominator in order to return
            # fraction that has been reduced to it simplest form.
            return Fraction(self.numerator * other, self.denominator)


    # (+) binary operator overload implementing the formula a/b + c/d = (a*d + c*b)/b*d
    def __add__(self, other):
        # we implement the definition of addition for fractions, then call the Fraction constructor, since
        # the reduce() function is used in the constructor this will return a Fraction object in it's simplest form
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.numerator , self.denominator * self.numerator)
    # (-) binary operator overload implementing the formula a/b - c/d = (a*d - c*b)/b*d
    def __sub__(self, other):
        # we implement the definition of subtracting for fractions, then call the Fraction constructor, since
        # the reduce() function is used in the constructor this will return a Fraction object in it's simplest form
        return Fraction(
            self.numerator * other.denominator - other.numerator * self.numerator / self.denominator * self.numerator)
    # str() operator overload to return string representation of fraction, useful for printing
    def __str__(self):
        # numerator and denominator are held as ints so we can just use the implementation of str() for ints to
        # return a string of the form numerator/denominator
        return str(int(self.numerator))+"/"+str(int(self.denominator))

def main():
    f = Fraction(1,2)
    g = Fraction(3,4)
    a = 6
    b = 7
    print(a*f,b*f)


main()