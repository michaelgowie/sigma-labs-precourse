def digitize(n):
    list_of_digits = list(str(n))
    for i in range(len(list_of_digits)):
        list_of_digits[i] = int(list_of_digits[i])
    return list_of_digits[::-1]
