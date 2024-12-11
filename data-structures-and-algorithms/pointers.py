# the variables here points to different places in memory
# when changing a variable specific value you uses more moemory

number_1 = 1
number_2 = number_1

print(f'number_1 points to : {id(number_1)}')
print(f'number_2 points to : {id(number_2)}')

number_2 = 2

print(f'number_1 points to : {id(number_1)}')
print(f'number_2 points to : {id(number_2)}')

# when using dictionaries you allocate the variables at same memmory
# the pointers are directed to the same space that the previous variable was

dict_1 = {'value': 1}
dict_2 = dict_1

print(f'dict_1 points to : {id(dict_1)}')
print(f'dict_2 points to : {id(dict_2)}')

dict_2['value'] = 2

print(f'dict_1 points to : {id(dict_1)}')
print(f'dict_2 points to : {id(dict_2)}')
