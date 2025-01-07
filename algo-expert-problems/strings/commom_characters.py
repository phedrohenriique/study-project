# CODE RUNS WITH BIGO -> O(n²)
# might have some improvement

def commonCharacters(strings):
    # Write your code here.
    my_hash = {}
    my_list = []

    for s_list in strings:
        for s in s_list:
            my_hash[s] = True

        for k,v in my_hash.items():
            if k not in s_list:
                my_hash[k] = False


    for k in my_hash:
        if my_hash[k]:
            my_list.append(k)
        
    return my_list