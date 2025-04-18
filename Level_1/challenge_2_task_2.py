import random


def reverse_name(name=str):
    return name[::-1]


def intersperse_name(first_name=str, surname=str):
    reversed_first_name = reverse_name(first_name)
    interspersed_name = ''
    min_name_length = min([len(first_name), len(surname)])
    for i in range(min_name_length):
        interspersed_name += reversed_first_name[i] + surname[i]
    if len(surname) == min_name_length:
        interspersed_name += reversed_first_name[min_name_length:]
    else:
        interspersed_name += surname[min_name_length:]
    return interspersed_name


def format_name(name=str):
    halfway = len(name) // 2
    split_name = name[:halfway] + ' ' + name[halfway:]
    return split_name.title()


def generate_from_name():
    first_name = input('What is your first name?')
    surname = input('What is your surname?')
    interspersed_name = intersperse_name(first_name, surname)
    formatted_name = format_name(interspersed_name)
    return (formatted_name)


def generate_randomly():
    username = ''
    string_of_characters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    print(len(string_of_characters))
    for i in range(10):
        username += random.choice(string_of_characters)
    username = username[:5] + ' ' + username[5:]
    return username


generation_choice = 0
while generation_choice not in ['1', '2']:
    generation_choice = input(
        'Enter 1 to generate a username from your name. Enter 2 to generate a random username.')
if generation_choice == '1':
    username = generate_from_name()
else:
    username = generate_randomly()

print(f'Your username is: {username}')
