word = "python"
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        attempts -= 1
    print(" ".join(guessed), f"Attempts left: {attempts}")

if "_" not in guessed:
    print("You won!")
else:
    print("You lost! The word was", word)
