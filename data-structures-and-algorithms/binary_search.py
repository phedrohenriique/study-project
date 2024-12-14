
# ARRAY MUST BE SORTED
# BIG O -> O(log n)

def binary_search(target, search_list, low_index, high_index):
    middle_index = (low_index + high_index)//2
    if low_index > high_index:
        print("TARGET NOT FOUND")
        return False
    if search_list[middle_index] == target:
        print(f'TARGET FOUND AT INDEX {middle_index}')
        return True
    if search_list[middle_index] > target:
        return binary_search(target, search_list, low_index, middle_index-1)
    if search_list[middle_index] < target:
        return binary_search(target, search_list, middle_index+1, high_index)


if __name__ == "__main__":
    my_target = 9
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_low_index = 0
    my_high_index = len(my_list)-1
    binary_search(my_target, my_list, my_low_index, my_high_index)
