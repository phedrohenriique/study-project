
nums = [2, 7, 11, 15]
target = 9

def problem_resolution(nums, target):
    solution = None
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j] == target - nums[i]:
                
                solution = [i, j]
                print(solution)
                return solution
    

if __name__ == "__main__":
    print("script running")
    problem_resolution(nums, target)
