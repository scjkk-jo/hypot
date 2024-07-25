# Requirements

# 2 inputs, positive, float or integer 
# 1 output, float
# external library? No external library
# create a function- calculate hypot = sqrt(a^2+b^2)
# Create a square root function: receives positive number, returns a float.

#def hypot(a, b):
#    return str((a**2 + b**2)**0.5)
#    return (a**2 + b**2)**0.5

def hypot(a, b):
    # docstring
    """This is a hypot function

    Args:
        a (int, float): side of triangle
        b (int, float): side of triangle

    Returns:
        float: hypotenuse
    """
    return sqrt(a**2 + b**2)
#    return 5.0

def sqrt(a):
    # docstring
    """This is a sqrt function that works by selecting the absolute value and returning the square root

    Args:
        a (int, float): pos or neg
    Returns:
        _type_: _description_
    """
    return abs(a)**0.5
#    return 2.0

#print(hypot(2.8,3.9))  # should be 5
#print(hypot(3,4)/hypot(3,4))  # we don't want a string
#print(hypot(3,4) + hypot(3,4))  # !

#print(sqrt(5.9))


