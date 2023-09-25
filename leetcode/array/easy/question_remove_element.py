nums = [1,3,6]
target = 5

def problem_resolution(nums, target):
    hash_map={}
    if target in nums:
        print(nums.index(target))
        return nums.index(target)
    else:
        for number in nums:
            if target < number:
                hash_map.setdefault('small', number)
            if target > number:
                hash_map.setdefault('big', number)
        if target > hash_map.get("low") and target < hash_map.get("big"):
            return nums.index(hash_map.get("low"))+1
        if target < hash_map.get("low") and (hash_map.get("big") == None):
            return nums.index(hash_map.get("low"))
        if target > hash_map.get("big") and (hash_map.get("low") == None):
            return nums.index(hash_map.get("big"))
        
if __name__ == "__main__":
    print("script running")
    problem_resolution(nums, target)
