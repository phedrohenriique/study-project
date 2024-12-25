my_dict = {
    0: 5,
    1: 4
}

list1 = [1, 2, 3]
list2 = [4, 5, 6]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def testing_loops():
    for n1, n2 in zip(list1, list2):
        print(n1, n2)


def simple_queue():
    pass


matrix = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

transposed_matrix = []

my_nested_list = [1,2,[3,4]]

if __name__ == "__main__":
    # print(my_list[0:5][1:2])
    # print(len(my_list))
    # print(my_list[0:9])
    # print(int(len(my_list[0:5][1:2]))//2)
    #transposed_matrix[0][0] = matrix[0][0]
    #print(transposed_matrix)
    #pass

    for n in my_nested_list:
        if hasattr(n,'__iter__'):
            print(n)
