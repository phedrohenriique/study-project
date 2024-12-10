from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    # numbers are equal
    # the index of the first is less than the next
    # nums = [1,2,3,1,1,3]

    hash_table = {}
    pair_list = []
    for n in range(len(nums)):  # len already gets index
        index_n = n
        number_n = nums[n]

        if index_n not in hash_table:
            hash_table[index_n] = number_n

    for k in hash_table:
        for i in range(len(nums)):
            if hash_table[k] == nums[i]:
                pass
            else:
                if hash_table[k] == nums[i] and k < i:
                    pair_list.append([k, i])

    print(pair_list)
    return len(pair_list)


if __name__ == "__main__":

    print(numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))
