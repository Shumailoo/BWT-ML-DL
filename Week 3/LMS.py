# LMS.py

class Book:
    def __init__(self, title, author, pages):
        """
        Book class with the attributes title, author, and pages.
        """
        self.title = title
        self.author = author
        self.pages = pages

    def get_title(self):
        """
        Returns the title of the book.
        """
        return self.title

    def set_title(self, new_title):
        """
        Sets the title of the book.
        """
        self.title = new_title

    def get_author(self):
        """
        Returns the author of the book.
        """
        return self.author

    def set_author(self, new_author):
        """
        Sets the author of the book.
        """
        self.author = new_author

    def get_pages(self):
        """
        Returns the number of pages in the book.
        """
        return self.pages

    def set_pages(self, new_pages):
        """
        Sets the number of pages in the book.
        """
        self.pages = new_pages

    @classmethod
    def reading_time(cls, pages, words_per_page=250):
        """
        Calculates the reading time for the number of words read in this book.
        Default reading speed is 250 words per minute.
        
        Args:
            pages (int): Number of pages in the book.
            words_per_page (int): Average number of words per page.

        Returns:
            float: Estimated reading time in minutes.
        """
        if not isinstance(pages, int) or not isinstance(words_per_page, int):
            raise ValueError("Pages and words per page must be integers.")
        if pages <= 0 or words_per_page <= 0:
            raise ValueError("Pages and words per page must be positive integers.")
        return (pages * words_per_page) / 250

    def __str__(self):
        """
        Method overridden to print all the attributes of the current Book.
        
        Returns:
            str: Formatted string with all attributes of the book.
        """
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Pages: {self.pages}\n"
        )


class EBook(Book):
    def __init__(self, title, author, pages, format):
        """
        EBook as a child class of Book with an additional attribute format.

        Args:
            title (str): The title of the ebook.
            author (str): The author of the ebook.
            pages (int): The number of pages in the ebook.
            format (str): The format of the ebook (e.g., 'pdf', 'epub').
        """
        super().__init__(title, author, pages)
        self.format = format

    def __str__(self):
        """
        Method overridden to print all the attributes of the current EBook.
        
        Returns:
            str: Formatted string with all attributes of the ebook.
        """
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Pages: {self.pages}\n"
            f"Format: {self.format}\n"
        )

if __name__=="__main__":
    # Demonstrate Book usage
    my_book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 195)
    print(f"Book title: {my_book.get_title()}")

    my_book.set_title("A New Book Title")
    print(f"Book title after change: {my_book.get_title()}")

    estimated_time = Book.reading_time(my_book.get_pages(), 300)  # Class method
    print(f"Estimated reading time (300 words per page): {estimated_time:.2f} minutes")


# Demonstrate EBook usage
    my_ebook = EBook("The Lord of the Rings", "J.R.R. Tolkien", 1178, "epub")
    print(my_ebook)
