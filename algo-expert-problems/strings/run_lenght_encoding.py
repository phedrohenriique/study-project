# THIS ANSWER IS WRONG
# IT NEEDS TO COUNT THE ELEMENTS IN SEQUENCE
# THE ELEMENTS ARE BEING COUNTED AS INDIVIDUALS
# USE STACK TO KEEP TRACK

def runLengthEncoding(string):
    new_element = string[0]
    element_list = []
    element_list.append(new_element)
    for e in string:
        if new_element is not e:
            element_list.append(e)
            new_element = e
    print(element_list)
    hash_list = {}
    for e in element_list:
        hash_list[e] = string.count(e)
    print(hash_list)
    new_string = ''
    for k, v in hash_list.items():
        if v > 9 :
            long_run = v // 9
            for n in range(long_run):
                new_string = new_string + f'9{k}'
            small_run = v % 9
            new_string = new_string + f'{small_run}{k}'
        else:
            new_string = new_string + f'{v}{k}'
    print(new_string)
    return new_string