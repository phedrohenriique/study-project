### BIG O CASES

# O(1)

def add_items(n):
    return n + n + n
 

print(add_items(10))

# O(A + B)

def print_items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

print_items(1, 10)

# O(n²)

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j) 

print_items(10)

# O(n² + n)
