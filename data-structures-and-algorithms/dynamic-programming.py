counter = 0

def fibonacci_sequence(n):
    global counter
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    sequence = [1, 1]
    for num in range(2, n):
        counter +=1
        sequence.append(sequence[-1]+sequence[-2])
    print(f'total counter {counter}')
    return sequence


if __name__ == "__main__":
    print(fibonacci_sequence(1))
    print(fibonacci_sequence(2))
    print(fibonacci_sequence(3))
    print(fibonacci_sequence(5))
    print(fibonacci_sequence(40))
