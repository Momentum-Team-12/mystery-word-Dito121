import random


def play_game():
    difficulty = 'difficulty'
    while True:
        difficulty = input(
            "Please choose your desired difficulty level. Your options are: \n easy: 4-6 letter word,\n normal: 6-8 letter word \n hard: 8+ letter word \n my difficulty choice: ")
        if difficulty.lower() == 'easy' or difficulty.lower() == 'normal' or difficulty.lower() == 'hard':
            break

    mystery_word = get_mystery_word(difficulty)
    display = '_'*len(mystery_word)
    guesses_remaining = 8
    previous_guesses = {}

    print("The mystery word contains {} letters.".format(len(mystery_word)))

    while guesses_remaining > 0:
        print("You have {} guesses remaining.".format(guesses_remaining))
        guess = str(input("Please guess a letter: ")).upper()

        if len(guess) > 1:
            print(f"{guess} is an invalid guess, please guess one letter at a time.")
            print(display)
            continue

        if previous_guesses.get(guess) == 1:
            print("You have already guessed {}, please try again.".format(guess))
            print(display)
            continue

        previous_guesses[guess] = 1

        if guess not in mystery_word:
            print(f"{guess} is not in the mystery word.")
            guesses_remaining -= 1
            print(display)
            continue

        for i in range(len(display)):
            if mystery_word[i] == guess:
                display = display[:i] + guess + display[i+1:]

        print("You have guessed a letter in the mystery word!")
        print(display)

        if display == mystery_word:
            print("Congratulations, you have uncovered the mystery word!")
            break

    if guesses_remaining == 0:
        print("Game Over, you have run out of guesses.")
        print(f"The mystery word was {mystery_word}")

    play_again = input("Do you want to play again?")
    if play_again.lower() == 'yes' or play_again.lower() == 'y':
        play_game()


def get_mystery_word(difficulty):
    with open('words.txt', 'r') as f:
        min = 0
        max = 0
        if difficulty == 'easy':
            min = 4
            max = 6
        elif difficulty == 'normal':
            min = 6
            max = 8
        else:
            min = 8
            max = 25

        lines = f.readlines()
        mystery_word = ''

        while not min <= len(mystery_word) <= max:
            line = lines[random.randint(0, len(lines) - 1)]
            line = line.split()
            mystery_word = line[random.randint(0, len(line) - 1)].upper()
        return mystery_word


if __name__ == "__main__":
    play_game()
