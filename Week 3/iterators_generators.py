import random

class Countdown:
    """
    Iterator class that counts down from a given number to 1.
    """
    def __init__(self, start):
        """
        Initializes the countdown iterator.
        
        Args:
            start (int): The number to start the countdown from.
        """
        self.current = start

    def __iter__(self):
        """
        Returns the iterator object itself.
        
        Returns:
            Countdown: The iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next number in the countdown.
        
        Returns:
            int: The next number in the countdown.
        
        Raises:
            StopIteration: When the countdown reaches below 1.
        """
        if self.current < 1:
            raise StopIteration
        else:
            current = self.current
            self.current -= 1
            return current


def fibonacci_generator(limit):
    """
    Generator function that yields Fibonacci numbers up to a specified limit.
    
    Args:
        limit (int): The upper limit for Fibonacci numbers.
    
    Yields:
        int: The next Fibonacci number.
    """
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def random_number_generator(low, high, count):
    """
    Generator function that yields a sequence of random numbers between a specified range.
    
    Args:
        low (int): The lower bound of the range.
        high (int): The upper bound of the range.
        count (int): The number of random numbers to generate.
    
    Yields:
        int: A random number within the specified range.
    """
    for _ in range(count):
        yield random.randint(low, high)


def main():
    # Demonstrate Countdown iterator
    print("Countdown from 5:")
    countdown = Countdown(5)
    try:
        for number in countdown:
            print(number)
    except Exception as e:
        print(f"Error during countdown: {e}")

    # Demonstrate fibonacci_generator
    print("\nFibonacci numbers up to 50:")
    try:
        for fib_number in fibonacci_generator(50):
            print(fib_number)
    except Exception as e:
        print(f"Error during Fibonacci generation: {e}")

    # Demonstrate random_number_generator
    print("\nRandom numbers between 1 and 10 (5 numbers):")
    try:
        for random_number in random_number_generator(1, 10, 5):
            print(random_number)
    except Exception as e:
        print(f"Error during random number generation: {e}")


if __name__ == "__main__":
    main()
