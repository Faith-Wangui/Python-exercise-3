class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = False  # Initially, the book is not borrowed

    def borrow_book(self):
        if not self.borrowed:
            self.borrowed = True
            print(f'Book "{self.title}" has been borrowed.')
        else:
            print(f'Book "{self.title}" is already borrowed.')

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(f'Book "{self.title}" has been returned.')
        else:
            print(f'Book "{self.title}" was not borrowed.')

    def display_info(self):
        status = "Borrowed" if self.borrowed else "Available"
        print(f'Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Status: {status}')

# Example usage
book1 = Book("The Mafias Obsession", "F. Scott James", 1955)
book1.display_info()

book1.borrow_book()
book1.display_info()

book1.return_book()
book1.display_info()
