import random


def play_game():
    random_word = get_random_word()
    print(random_word)


def get_random_word():
    with open('words.txt', 'r') as f:
        lines = f.readlines()
        line = lines[random.randint(0, len(lines) - 1)]
        line = line.split()
        return line[random.randint(0, len(line) - 1)]


if __name__ == "__main__":
    play_game()
