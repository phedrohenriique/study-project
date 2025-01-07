def isPalindrome(string):
    counter = -1
    middle = int(len(string))

    if len(string) == 1:
        return True
        
    for s in range(middle):
        if string[s] == string[counter]:
            counter -=1
            continue
        elif string[s] == string[-s-1]:
            continue
        else:
            return False
    return True