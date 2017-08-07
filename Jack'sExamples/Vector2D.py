"""
implementation of a simple vector3D class with very basic functionality in order to demonstrate operator overloading
note the use of __something__() to overload the operators
"""

class Vector3D(object):

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    # first example of operator overloading, here we overload the str() conversion operator
    def __str__(self):
        return "["+str(self.x)+", "+str(self.y)+", "+str(self.z)+"]"

    # here we overload the + operator, this has an obvious interpretation for vectors
    def __add__(self, other):
        return Vector3D(self.x+other.x,self.y+other.y,self.z+other.z)

    # here we overload the - operator, this also has an obvious interpretation for vectors
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    """
     here we overload the * operator, this is more problematic. What does it mean to "multiply" two vectors? 
     We have to choose either the scalar product or the cross product
     However it is not clear from the syntax "*" which we mean, and it certainly isn't clear to someone else 
     Using your code who might not have access to the class file. In reality you should only overload operators
     if it is absolutely clear what it means for your specific object, if in doubt use a method with an appropriate  
     name instead to make it clear. Here we overload * with the scalar product for illustrative purposes.
    """
    def __mul__(self, other):
        return self.x*other.x+self.y*other.y+self.z*other.z

def main():
    u = Vector3D(1,2,3)
    v = Vector3D(4,5,6)

    print(str(u)+ " + " + str(v) +  " = " + str(u+v))
    print(str(u) + " - " + str(v) + " = " + str(u - v))
    print(str(u) + " dot " + str(v) + " = " + str(u * v))

main()


