# main.py
from mymath import add, subtract, multiply, divide, modulus, exponentiate, sqrt

def main():
    # Demonstrate basic arithmetic operations
    try:
        print("Addition of 5 and 3:", add(5, 3))
        print("Subtraction of 5 from 8:", subtract(8, 5))
        print("Multiplication of 5 and 3:", multiply(5, 3))
        print("Division of 10 by 2:", divide(10, 2))
        print("Modulus of 10 by 3:", modulus(10, 3))
        print("Exponentiation of 2 to the power 3:", exponentiate(2, 3))
        print("Square root of 16:", sqrt(16))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()