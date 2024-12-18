unsorted_list = [4, 6, 1, 7, 3, 2, 5]


def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list:list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)

    return swap_index  


def quick_sort(mylist, left, right):
    if left < right:
        pivot_index = pivot(mylist, left, right)
        quick_sort(mylist, left, pivot_index-1)
        quick_sort(mylist, pivot_index+1, right)
    return mylist


print(quick_sort(unsorted_list, 0, 6))

## BIG 0 -- > 0(n log n) worst condition, if list is sorted -- > 0(n^n)
