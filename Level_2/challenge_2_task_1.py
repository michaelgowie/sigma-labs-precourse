from random import randint


def take_guess_from_user(num_to_guess):
    while True:
        try:
            guess = input('What is your guess?')
            guess = int(guess)
            break
        except:
            print('Your guess must be an integer, try again.')
    if guess > num_to_guess:
        print('Too High!')
    elif guess < num_to_guess:
        print('Too low!')
    else:
        print('That\'s Correct!')
    return guess


def run_game():
    num_to_guess = randint(1, 50)
    print('I\'ve chosen a number between 1 and 50. It\'s up to you to guess!')
    guess = 51
    list_of_guesses = []
    while guess != num_to_guess:
        guess = take_guess_from_user(num_to_guess)
        if guess not in list_of_guesses:
            list_of_guesses.append(guess)
    attempts = len(list_of_guesses)
    print(
        f'Congratulations! You guessed the number was {num_to_guess}. You took {attempts} guesses.')


run_game()
