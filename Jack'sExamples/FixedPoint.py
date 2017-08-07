"""
class to represent a "fixed point" number; number with a fixed number of decimal places, in this case two
if we represent a fixed point to two decimal places as base.decimal, the class is implemented by having two member
variables "base" and "decimal" which are held as ints
"""

class FixedPoint(object):
    # constructor will take different numbers of arguments depending on whether we choose to initialise our fixed
    # point with a float or with "base" and "decimal" arguments
    def __init__(self,*args):
        # if we feed the constructor two arguments assume it jas been given a base and decimal
        if(len(args)==2):
            # make first argument base of fixed point
            base = args[0]
            self.base = base
            # make second argument decimal part of fixed point
            decimal = args[1]
            self.decimal = decimal

            # if either the base or decimal part is negative we take the whole number to be negative. It is easiest to
            # implement addition for negative fixed point by making both the base and the decimal parts negative
            # this is clear by going through an explicit example on paper of adding two fixed points where one is
            # negative
            if(base<0 or decimal < 0):
                if(base>0):
                    self.base = -base
                if(decimal>0):
                    self.decimal = -decimal
        # if the constructor receives only one argument we assume we want to construct a fixed point from a floating
        # point variable
        if(len(args)==1):
            d = args[0]
            # convert the float into an int to get the base
            self.base = int(d)
            # to get the decimal part:
            #1 d - base leaves the fractional component of the float
            #2 *100 to move two digits of the decimal past the decimal point
            #3 round it to get the accuracy to 2.d.p.
            #4 finally convert to int to drop any trailing 0 past the decimal point
            self.decimal = int(round((d-self.base)*100))
    # float() operator overload to convert FixedPoint to a float, this will be useful for implementing the str() method
    def __float__(self):
        # convert decimal to float so we can do floating point division, divide by 100 to get the decimal component
        # of the float, then add the base. Automatic conversions insure that base is converted to a float before the
        # addition, so the number returns will be a float with two decimal places.
        # this implementation requires that for negative FixedPoints both the base and decimal varibles are negative,
        # since they are added together
        return self.base+float(self.decimal)/100

    # (==) operator overload to test whether two FixedPoint instances are equal
    def __eq__(self, other):
        # We consider the two instances equal if their base and decimal components are the same
        return(self.base == other.base and self.decimal == other.decimal)
    # str() operator overload to convert the FixedPoint to a string, useful for printing
    def __str__(self):
        # implemented by first converting the FixedPoint instance to a float using the float() operator overload we
        # wrote above, then use the str() operator for float to return string conversion of the FixedPoint
        return str(FixedPoint.__float__(self))
    # (+) binary operator overload to add two FixedPoints
    def __add__(self, other):
        # implemented by converting to a float using float() overload then adding floats and calling the FixedPoint
        # constructor to return a FixedPoint
        return FixedPoint(FixedPoint.__float__(self)+FixedPoint.__float__(other))
    # (-) binary operator for subtracting one FixedPoint from another
    def __sub__(self, other):
        # implemented by converting to a float using float() overload then subtracting floats and calling the FixedPoint
        # constructor to return a FixedPoint
        return FixedPoint(FixedPoint.__float__(self) - float(other))
    # (-) unary operator for negation of a FixedPoint
    def __neg__(self):
        # call FixedPoint constructor on negation of base and decimal parts, actually only need to make one of base or
        # decimal negative due to the implementation of the constructor sign of both variables will be changed
        return FixedPoint(-self.base,-self.decimal)




f = FixedPoint(12.3)
g = FixedPoint(-1,23)
h = f+g
print(str(h))




