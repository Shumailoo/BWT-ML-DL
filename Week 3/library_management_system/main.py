from LMS import Book, EBook
# Demonstrate Book usage
try:
    my_book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 195)
    print(my_book)

    my_book.set_title("A New Book Title")
    print(my_book)

    estimated_time = Book.reading_time(my_book.get_pages(), 300)  # Class method
    print(f"Estimated reading time (300 words per page): {estimated_time:.2f} minutes")
except ValueError as e:
    print(f"Error: {e}")

# Demonstrate EBook usage
try:
    my_ebook = EBook("The Lord of the Rings", "J.R.R. Tolkien", 1178, "epub")
    print(my_ebook)
except ValueError as e:
    print(f"Error: {e}")
