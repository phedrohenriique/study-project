def one():
    two()
    print(1)


def two():
    three()
    print(2)


def three():
    print(3)

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
if __name__ == "__main__":
    #one()
    fac = factorial(10)
    print(fac)
