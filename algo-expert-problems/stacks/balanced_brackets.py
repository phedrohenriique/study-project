# Balanced Brackets problem
# check if the bracked below is balanced or not, the example
# returns a balanced bracket and one that it is not
# INPUT -> "{()}[]"
# OUTPUT -> True
# -------------------
# INPUT -> "{[}]"
# OUTPUT -> False

class StackInterview:

    def __init__(self) -> None:
        self.stack_list = []

    def stack_push(self, value):
        self.stack_list.append(value)

    def stack_pop(self):
        item = self.stack_list.pop()
        return item

    def stack_list(self):
        return self.stack_list


# INPUT -> "{()}[]"
opening_bracket = ["{", "[", "("]
closing_bracket_hash = {
    "}": "{",
    "]": "[",
    ")": "("
}


def balancedBrackets(string):
    my_stack = StackInterview()
    for item in string:
        if len(my_stack.stack_list) == 0 and item in closing_bracket_hash.keys():
            return False
        if item in opening_bracket:
            my_stack.stack_push(item)
            continue
        elif item not in ["{", "[", "(", ")", "]", "}"]:
            continue
        elif my_stack.stack_list[-1] is not closing_bracket_hash[item]:
            return False
        elif my_stack.stack_list[-1] == closing_bracket_hash[item]:
            my_stack.stack_pop()
    if len(my_stack.stack_list) > 0:
        return False
    return True
