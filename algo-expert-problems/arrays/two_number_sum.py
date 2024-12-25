def twoNumberSum(array, targetSum):
    # Write your code here.
    sum_hash = {}
    for n in array:
        sum_hash[n] = targetSum - n
        
    for k, v in sum_hash.items():
        if k == v:
            continue
        if v in array:
            return [k,v]
    return []
