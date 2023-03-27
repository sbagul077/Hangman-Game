import random

# load the file
with open("words_list.txt") as file:
    words = [word.strip() for word in file.readlines()]


# function of the random library

def get_word():
    return random.choice(words)


# function to show the progress of the game
def show_state(word, guesses, incorrect_guesses):
    # show the word with underscores for unguessed letters
    display_word = ""
    print(word, guesses)
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
        print(display_word)

        # show the wrong guesses
        if len(incorrect_guesses) > 0:
            print("Incorrect guesses : {}".format("".join(incorrect_guesses)))

        # draw the hang man
        print("")
        if len(incorrect_guesses) >= 1:
            print(" 0 ")

        if len(incorrect_guesses) == 2:
            print(" | ")
        elif len(incorrect_guesses) == 3:
            print(" \| ")
        elif len(incorrect_guesses) >= 4:
            print(" \|/ ")

        if len(incorrect_guesses) == 5:
            print(" /  ")
        elif len(incorrect_guesses) >= 6:
            print(" / \ ")


# create a function to play the game

def play():
    word = get_word()
    guesses = set()
    incorrect_guesses = list()
    max_incorrect_guesses = 7

    while True:
        # show the game
        show_state(word, guesses, incorrect_guesses)
        # get the players guess
        guess = input("Write a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid! Please enter just letter.")
            continue

        # look if the player has already guess

        if guess in guesses:
            print("Letter already used")
            continue

        # add the guess to guesses
        guesses.add(guess)

        # look if the guess is correct
        if guess in word:
            if set(word) == guesses:
                show_state(word, guesses, incorrect_guesses)
                print("Finally, You Win!!!")
                return
        else:
            incorrect_guesses.append(guess)
            if len(incorrect_guesses) == 4:
                print("You pass half of the way")
            elif len(incorrect_guesses) == 7:
                show_state(word, guesses, incorrect_guesses)
                print("Last Chance, use it carefully!")

            if len(incorrect_guesses) >= max_incorrect_guesses:
                show_state(word, guesses, incorrect_guesses)
                print("You have no idea about this game, do you? The word was '{}'.".format(word))
                return


# play the game
play()
