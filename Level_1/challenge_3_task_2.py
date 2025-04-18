def ask_user_for_number():
    while True:
        n = input('Give me a positive integer.')
        try:
            n = int(n)
            if n > 0:
                break
            else:
                print('Error: That\'s not positive.')
        except:
            print('Error: That was not an integer.')
    return n


def sum_up_to_n():
    n = ask_user_for_number()
    sum = int((n + 1) * (n / 2))
    print(sum)
    return (sum)


def sum_up_to_n_multiples_of_3_and_5():
    n = ask_user_for_number()
    sum = 0
    for i in range(3, n+1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)
    return (sum)


def product_or_sum():
    n = ask_user_for_number()
    answer = 0
    while answer not in ['1', '2']:
        answer = input(
            'Input 1 for the sum up to n. Input 2 for the product up to n.')
    if answer == '1':
        sum = int((n + 1) * (n / 2))
        print(sum)
        return (sum)
    else:
        prod = 1
        for i in range(2, n+1):
            prod *= i
        print(prod)
        return (prod)


product_or_sum()
