def max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
        elif number < minimum:
            minimum = number
    return [minimum, maximum]


if __name__ == "__main__":
    print(max_min([77, 8, -2, 8, 9.2, 120, -34]))
