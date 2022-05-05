from data_structures.stack import Stack


def multi_bracket_validation(string):
    brackets = {']':'[','}':'{',')':'('}
    new_stack = Stack()
    for char in string:
        if char not in brackets:
            new_stack.push(char)
        else:
            if new_stack.top == None:
                return False
                break
            if new_stack.top.value == brackets[char]:
                new_stack.pop()
            else:
                return False
                break
    if new_stack.is_empty:
        return True
    else:
        return False


# def multi_bracket_validation(string):
#     stack = []

#     for paren in string:
#         if paren == '(' or paren == '[' or paren == '{':
#             stack.append(paren)
#         else:
#             if not stack:
#                 return False
#             else:
#                 top = stack[-1]
#                 if paren == ')' and top == '(' or paren ==']' and top == '[' or paren == '}' and top == '{':
#                     stack.pop()

#     if not stack:
#         return True
#     else:
#         return False
