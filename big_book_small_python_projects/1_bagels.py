"""
In Bagels, a deductive logic game, you must guess a secret three-digit number
based on clues. The game offers one of the following hints in response to your guess:
“Pico” when your guess has a correct digit in the wrong place, “Fermi” when your guess has a correct
digit in the correct place, and “Bagels” if your guess has no correct digits. You have 10 tries to guess the
secret number.

I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.
I have thought up a number.
You have 10 guesses to get it.
Guess #1:
> 123
Pico
Guess #2:
> 456
Bagels
Guess #3:
> 178
Pico Pico
--snip--
Guess #7:
> 791
Fermi Fermi
Guess #8:
> 701
You got it!
Do you want to play again? (yes or no)
> no
Thanks for playing!

"""

import random

from typing import List

def generate_3_digit_number():
    return random.sample(['0', '1', '2', '3', '4', '5', '6'], 3)


def user_guess_input(guess_no):
    print(f"Guess #{guess_no}: ")
    num_in_string = input()
    if len(num_in_string) != 3:
        print("You need to enter three digit number. Exiting the game")
        exit(1)

    # check for only numerical values

    return num_in_string


def check_similarity(original_num: List, user_input=str):
    original_num_as_str = "".join(original_num)
    if original_num_as_str == user_input :
        print("You got it!")
        return True
    
    out = []

    for i, v in enumerate(original_num):
        if v in user_input:
            if v == user_input[i]:
                out.append("Fermi")
            else:
                out.append("Pico")
        
    if len(out) == 0:
        print("Bagels")
    else:
        # Sort is from original author
        out.sort()
        print(" ".join(out))

    return False


def ask_for_another_game():
    print("Do you want to play another game? - yes/no")
    res = input()
    if res == "yes":
        main()
    else:
        print("Thanks for playing")
        exit(0)


def main():
    print("I have thought up a number.\n"
            "You have 10 guesses to get it.")

    original_num = generate_3_digit_number()

    for i in range(1, 11):
        input = user_guess_input(i)
        similar = check_similarity(original_num, input)
        if similar:
            break
    else:
        print("You have exhausted all the guesses. Game will end")
        print(f"Original number was: {''.join(original_num)}")

    ask_for_another_game()


if __name__ == "__main__":
    main()

