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

class Car:

    motor = 2
    list_materials = ['steel', 'plastic', 'glass']

    def __init__(self, name) -> None:
        self.name = name


car_1 = Car('corola')

car_2 = Car('mitsubish')

# print('primeiro objeto :', car_1.motor)

# print('segundo objeto :', car_2.motor)

# print(id(car_2.list_materials))
# car_2.list_materials.pop()

# print(id(car_1.list_materials))

# print(id(car_1.name))
# print(id(car_2.name))

print(car_2)

livro = 'harry potter'

print('bom livro',f'{livro}')

