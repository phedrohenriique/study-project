class Book:
    """ A simple Book class """


# constructor for the class
    def __init__(self, title) -> None:
        self.title = title
# getter method for the class accessing the attribute title
    def get_title(self):
        return self.title
# setter method for the class accessing the atribute title
    def set_tile(self, title):
        self.title = title

book_one = Book('First Learning')
book_two = Book('Programming Language')

print(book_one.get_title())
print(book_two.get_title())

book_one.set_tile('Second Learning')

print(book_one.get_title())