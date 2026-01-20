import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    mid_index = len(poss_values) // 2
    return poss_values[mid_index]

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if user_input == "h":
        if next_val > current_val:
            return True
        else:
            return False
    elif user_input == "l":
        if next_val < current_val:
            return True
        else:
            return False


# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                board[i]
        print(f"Well done '{letter}' is in the word")
        return True
    else:
        print(f"Sorry, '{letter}' isn't in the word")
        return False