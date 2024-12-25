def caesarCipherEncryptor(string, key):
    additional_elements = []
    index_counter = key
    check_list = [
        'a','b','c','d','e','f','g','h',
        'i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z'
                  ]
    last_element_index = check_list.index(string[-1])

    print(last_element_index)
    
    for n in range(index_counter):
        if last_element_index == len(check_list)-1:
            last_element_index = 0
            continue
        last_element_index += 1
    print(last_element_index)
    for n in range(len(string)):
        additional_elements.append(check_list[last_element_index])
        if last_element_index == 0:
            last_element_index == len(check_list)-1
        last_element_index -=1
    additional_elements.reverse()
    new_string = ''
    
    for s in additional_elements:
        new_string += s
        
    return new_string