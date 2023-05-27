
def addTwoNumbers(l1, l2):

    def list_to_number(list):
        string_number = ""
        while list:
            string_number = string_number + str(list.val)
            list = list.next
        # for number in list:
        #     string_number = string_number + f"{number}"
        return int(string_number)

    def number_to_list(number):
        string_number = list(str(number))
        return string_number
        pass
    
    number_1 = list_to_number(l1)
    number_2 = list_to_number(l2)
    result = number_1 + number_2
    result_list = number_to_list(result)
    print(result_list)
    return result_list


# def list_to_number(list):
#             string_number = ""
#             while list:
#                 string_number = string_number + str(list.val)
#                 list = list.next
#             #for number in list:
#             #   string_number = string_number + f"{number}"
#             return int(string_number)

#         def number_to_list(number):
#             string_number = list(str(number))
#             return string_number
#             pass
    

#         def linked_list(list):
#             if not list:
#                 return None
#             head = ListNode(list[0])
#             current = head
#             for item in list[1:]:
#                 current.next = ListNode(item)
#                 current = current.next
#             return head

#         number_1 = list_to_number(l1)
#         number_2 = list_to_number(l2)
#         result = number_1 + number_2
#         result_list = number_to_list(result)
#         print(result_list)
#         result_list.reverse()
#         print(result_list)

#         return linked_list(result_list)

# l1 =
# [2,4,9]
# l2 =
# [5,6,4,9]

if __name__ == "__main__":
    print('script start')

    addTwoNumbers([2,4,3], [5,6,4])
