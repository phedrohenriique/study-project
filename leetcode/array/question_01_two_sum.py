
def twoSum( nums, target):

    target_goal = target
    nums_result = []

    for first_number in nums:
        target_goal = target_goal - first_number
        #print('first number : ', first_number)
        #print('goal : ', target_goal)
        for second_number in nums:
            #print('second number : ', second_number)
            #print('goal : ', target_goal)
            if (second_number == first_number) and (nums.count(second_number) == 1) :
                continue
            target_goal = target_goal - second_number
            if target_goal == 0:
                #print('found answer')
                nums_result.append(nums.index(first_number))
                if first_number == second_number:
                    nums.insert(nums.index(first_number), "double")
                nums_result.append(nums.index(second_number))
                nums_result.sort()
                print('answer : ', nums_result)
                return nums_result
            target_goal = target - first_number

if __name__ == "__main__":
    print('script start')
    #twoSum([2, 7, 11, 15], 9)
    #twoSum([3,2,4], 6)
    twoSum([3,3], 6)
