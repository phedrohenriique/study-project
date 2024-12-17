# buildings -> array of integers non zero = [1,2,3]
# building can see if is taller than all of the buildings in the direction it faces
# if it is right the array goes -> , if it is left it goes <-
# the array must be the indexes
# right = east
# left = west
# last or first will see independently

# 2 case 
#{
#  "buildings": [3, 5, 4, 4, 3, 1, 3, 2],
#  "direction": "WEST"
#}

# try to pass the test case 12 in algoexpert
# expected output -> [0, 1, 2, 4, 5, 6, 10, 13]
# code output -> [0, 1, 2, 4, 5, 12, 10, 13]
# question input -> 
#{
#  "buildings": [1, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8],
#  "direction": "WEST"
#}

# THE SOLUTION IS OPTMIZED BIG O -> O(n) for space and time

class StackInterview:
    
    def __init__(self):
        self.stack_list = []

    def stack_push(self, value):
        self.stack_list.append(value)

    def stack_pop(self):
        item = self.stack_list.pop()
        return item
    def print_stack(self):
        print(self.stack_list)
        
class HashInterview:
    def __init__(self):
        self.hash_map = {}

    def __getitem__(self, key):
        return self.hash_map[key]
        
    def __setitem__(self,key, value):
        self.hash_map[key] = value

def sunsetViews(buildings, direction):
    
    my_stack = StackInterview()
    my_hash_index = HashInterview()
    current_height = 0
    greatest_height = 0
    
    for i in range(len(buildings)):
        # needs to store a list value and compare with possible different indexes
        my_hash_index[buildings[i]]=i # height of building = key, index = value
            

    if len(buildings) == 0:
        return []
    if len(buildings) == 1:
        return [0]
    
    if direction == "EAST":  
        for i in range(len(buildings)): # checking height and do not check last
        #    current_height = buildings[i]
        #    if i < (len(buildings)-2):
        #        if current_height > buildings[i+1]:
        #            my_stack.stack_push(my_hash_index[current_height])
            if i == 0:
                continue
            if i*-1 == -1:
                greatest_height = buildings[-i]
                my_stack.stack_push(my_hash_index[buildings[-1]])
                continue
            opposite_index = i*-1
            if buildings[opposite_index] > greatest_height:
                my_stack.stack_push(my_hash_index[buildings[opposite_index]])
                greatest_height = buildings[opposite_index]

        if buildings[0] > greatest_height:
            my_stack.stack_push(0)

        my_stack.stack_list.sort()

    if direction == "WEST":
        for i in range(len(buildings)):
            current_height = buildings[i]
            print(f'current height: {current_height} and greatest:{greatest_height}')
            if i == 0:
                my_stack.stack_push(0)
                greatest_height = current_height
                continue
            if current_height > greatest_height:
                my_stack.stack_push(my_hash_index[current_height])
                greatest_height = current_height
                
    return my_stack.stack_list
