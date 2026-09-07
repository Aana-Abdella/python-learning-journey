def reverse_string(str1):
    rstr1 = ''
    index = len(str1)
    print(index)
    while index > 0:
        rstr1 += str1[index -1]
        print(str1[index - 1])
        index = index - 1
    return rstr1
print(reverse_string('hello world'))
