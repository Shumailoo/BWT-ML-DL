# modulus.py
def modulus(a, b):
    """
    Returns the remainder of a divided by b.
    
    Args:
        a (float): The numerator.
        b (float): The denominator.
    
    Returns:
        float: The remainder of a divided by b.
    
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a % b
