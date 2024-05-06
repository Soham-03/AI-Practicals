import random

def hangman():
    words = ["soham", "elephannt"]
    word = random.choice(words)
    guessed = '_' * len(word)
    guessed = list(guessed)
    word = list(word)
    attempts = 6

    while attempts > 0:
        print(' '.join(guessed))
        guess = input("Take a guess: ").lower()
        
        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed[index] = guess
                    print("Correct Guess")
            if '_' not in guessed:
                print("Won")
                print(f"Word was {word}")
        else:
            attempts -= 1
            print(f"Wrong Guess {attempts} attempts left")
        if attempts == 0:
            print("Lost:")

hangman()