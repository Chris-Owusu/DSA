

# # *_, = 'Python'
# # print(_)


# a, *b, c = 'Python'
# print(a)
# print(b)
# print(c)

# ast = "*****"
# lst = []

# def solution(picture):
#     lst.append(ast)  # Use append() instead of push() to add elements to the list
#     for elem in picture:
#         if len(elem) == 3:
#             lst.append('*' + elem + '*')  # Add modified element to the list
#         else:
#             lst.append('*' + elem[0:3] + '*')  # Modify and add the element to the list
#     lst.append(ast)  # Add the last asterisk line to the list
#     return lst

# pic = ["asd", "abc", "cdf"]  # "cdf" instead of "ded" to match the desired output

# result = solution(pic)

# for line in result:
#     print(line)


def solution(picture):
    width = max(len(elem) for elem in picture) + 2
    result = ['*' * width] + ['*' + elem + '*' for elem in picture] + ['*' * width]
    return result

pic = ["asd", "abc", "ded"]

result = solution(pic)

formatted_result = [f'"{line}",' for line in result]

print("[" + "\n".join(formatted_result)[:-1] + "]")

