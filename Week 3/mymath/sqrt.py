import math# sqrt.py


def sqrt(a):
    """
    Returns the square root of a.
    
    Args:
        a (float): The number to find the square root of.
    
    Returns:
        float: The square root of a.
    
    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)
