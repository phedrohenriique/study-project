# the variables here points to different places in memory
# when changing a variable specific value you uses more moemory

number_1 = 1
number_2 = number_1

print(f'number_1 points to : {id(number_1)}')
print(f'number_2 points to : {id(number_2)}')

number_2 = 2

print(f'number_1 points to : {id(number_1)}')
print(f'number_2 points to : {id(number_2)}')