# file_handling.py

def read_file(file_path):
    """
    Reads data from a text file and prints its contents.
    Also counts the number of words in the file and prints the result.
    
    Args:
        file_path (str): Path to the text file.
    """
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("File Contents:\n", contents)
            
            # Counting the number of words in the file
            word_count = len(contents.split())
            print(f"\nNumber of words in the file: {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An error occurred while reading the file '{file_path}'.")

def write_to_file(file_path, user_input):
    """
    Writes user input to a new file.
    
    Args:
        file_path (str): Path to the output file.
        user_input (str): Input provided by the user to write to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(user_input)
            print(f"User input successfully written to '{file_path}'")
    except IOError:
        print(f"Error: An error occurred while writing to the file '{file_path}'.")

if __name__ == "__main__":
    # Demonstrate reading from 'data.txt'
    read_file('data.txt')
    
    # Get user input and write to 'output.txt'
    user_input = input("Enter some text to write to 'output.txt': ")
    write_to_file('output.txt', user_input)
