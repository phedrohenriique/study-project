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

def fib(n):
    # Write your code here.
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3 :
        return 1
    return fib(n-1)+fib(n-2)
if __name__ == "__main__":
    #one()
    #fac = factorial(10)
    #print(fac)
    print(fib(5))
