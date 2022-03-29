import random
import os
import time as t
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generate_frequencies() -> dict[str: dict[str: int]]:
    tic = t.perf_counter()
    freqs = {}
    for char in ALPHA:
        freqs[char] = {}
    for filename in os.listdir("Texts"):
        with open("Texts" + filename, "r", encoding = "utf8") as file:
            for line in file:
                line.removesuffix("\n")
                line = line.upper()
                i = 0
                while i < len(line) - 1:
                    if line[i] in ALPHA and line[i+1] in ALPHA:
                        if freqs[line[i]].get(line[i+1]):
                            freqs[line[i]][line[i+1]] += 1
                        else:
                            freqs[line[i]][line[i+1]] = 1
                    i += 1
    toc = t.perf_counter()
    print(f"Frequencies generated in {toc-tic :0.4f} seconds")
    return freqs

def generate_word(freqs) -> str:
    """Creates random 'word' of length 5"""
    word = random.choice(list(ALPHA))
    while len(word) != 5:
        possible_dict = freqs[word[-1]]
        next = random.choices(list(possible_dict.keys()), weights = list(possible_dict.values()), k = 1)
        word += next[0]
    return word

def play():
    freqs = generate_frequencies()
    answer = generate_word(freqs)
    print("STRINGLE\n--------")
    guess = input()
    guess = guess.upper()
    keyboard = {}
    for char in ALPHA:
        keyboard[char] = ""
    guesses = 0
    while guess != answer:
        if guess == "K":
            for key in keyboard:
                print(key + ": " + keyboard[key])
        elif len(guess) == 5:
            guesses += 1
            for i, char in enumerate(guess):
                if char == answer[i]:
                    print("🟩", end = "")
                    keyboard[char] = "🟩"
                elif char in answer:
                    print("🟨", end = "")
                    if keyboard[char] != "🟩":
                        keyboard[char] = "🟨"
                else:
                    print("🟪", end = "")
                    if keyboard[char] == "":
                        keyboard[char] = "🟪"
            print()
        guess = input("").upper()
    print("🟩🟩🟩🟩🟩")
    print(guesses)

play()
