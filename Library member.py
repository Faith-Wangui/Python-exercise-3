class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = False  # Initially, the book is not borrowed

    def borrow_book(self):
        if not self.borrowed:
            self.borrowed = True
            return True  # Successfully borrowed
        return False  # Already borrowed

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return True  # Successfully returned
        return False  # Was not borrowed

    def display_info(self):
        status = "Borrowed" if self.borrowed else "Available"
        print(f'Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Status: {status}')


class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # List to store borrowed books

    def borrow_book(self, book):
        if book.borrow_book():  # Check if book can be borrowed
            self.borrowed_books.append(book)
            print(f'{self.name} has borrowed "{book.title}".')
        else:
            print(f'Sorry, "{book.title}" is already borrowed.')

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                print(f'{self.name} has returned "{book.title}".')
        else:
            print(f'{self.name} does not have "{book.title}" borrowed.')

    def display_info(self):
        print(f'Member ID: {self.member_id}, Name: {self.name}')
        print("Borrowed Books:")
        if self.borrowed_books:
            for book in self.borrowed_books:
                print(f'- {book.title} by {book.author}')
        else:
            print("No books borrowed.")


# Example usage
book1 = Book("Atomic Habits", "F. David Nowel", 1975)
book2 = Book("1981", "George Nerbert", 1950)

member1 = LibraryMember(1, "Alice")

# Borrowing books
member1.borrow_book(book1)
member1.borrow_book(book2)

# Display member info
member1.display_info()

# Returning a book
member1.return_book(book1)
member1.display_info()
