import random

def hangman():
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]
    word = random.choice(word_list)
    guessed = "_" * len(word)
    guessed = list(guessed)
    word = list(word)
    attempts = 6

    while attempts > 0:
        print(' '.join(guessed))
        guess = input("Guess a letter: ").lower()
        
        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed[index] = guess
            if "_" not in guessed:
                print("Congratulations! You won!")
                print("The word was: " + ''.join(word))
                break
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")
        
        if attempts == 0:
            print("You lost! The word was: " + ''.join(word))

if __name__ == "__main__":
    hangman()
