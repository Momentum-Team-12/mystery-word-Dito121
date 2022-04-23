import random


def play_game():
    random_word = get_random_word()
    display = '_'*len(random_word)
    guesses_remaining = 8
    previous_guesses = {}

    print("The mystery word contains {} letters.".format(len(random_word)))

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

        if guess not in random_word:
            print(f"{guess} is not in the mystery word.")
            guesses_remaining -= 1
            print(display)
            continue

        for i in range(len(display)):
            if random_word[i] == guess:
                display = display[:i] + guess + display[i+1:]

        print("You have guessed a letter in the mystery word!")
        print(display)

        if display == random_word:
            print("Congratulations, you have uncovered the mystery word!")
            break

    if guesses_remaining == 0:
        print("Game Over, you have run out of guesses.")
        print(f"The mystery word was {random_word}")


def get_random_word():
    with open('words.txt', 'r') as f:
        lines = f.readlines()
        line = lines[random.randint(0, len(lines) - 1)]
        line = line.split()
        return line[random.randint(0, len(line) - 1)].upper()


if __name__ == "__main__":
    play_game()
