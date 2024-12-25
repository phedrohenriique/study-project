def sortedSquaredArray(array):
    # Write your code here.
    new_array = [(sqn**2) for sqn in array]
    new_array.sort()
    return new_array