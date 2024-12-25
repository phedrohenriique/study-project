# INPUT -> array = [1, 0, 0, -1, -1, 0, 1, 1], order = [0, 1, -1]
# OUTPUT -> [0, 0, 0, 1, 1, 1, -1, -1]
# The idea is to use BIG O -> O(n) 
# for that the loop shall not be nested but instead out of each other
# a hint is to use a counter with the array other and iterate each value

def threeNumberSort(array, order):
    sorted_array = []
    for num_order in order:
        for n in array:
            if n == num_order:
                sorted_array.append(n)
    return sorted_array