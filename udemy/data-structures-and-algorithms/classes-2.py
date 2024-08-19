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

