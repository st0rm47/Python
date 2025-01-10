import random

class Hangman:
    def __init__(self):
        self.words = ["PYTHON", "HANGMAN", "COMPUTER", "PROGRAMMING", "DEVELOPER"]
        self.word = random.choice(self.words) 
        self.guessed_word = ["_"] * len(self.word) 
        self.lives = 6  
        self.guessed_letters = []

    def display_state(self):
        print("\nCurrent word:", " ".join(self.guessed_word))
        print("Lives remaining:", self.lives)
        print("Guessed letters:", ", ".join(self.guessed_letters))

    def play(self):
        print("Welcome to Hangman!")
        print("Try to guess the word, one letter at a time.")
        print("_ " * len(self.word))
        
        while self.lives > 0:
            self.display_state()
            guess = input("Enter a letter: ").upper()

            # Checks if the input is a single letter and is an alphabet
            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single valid letter.")
                continue

            if guess in self.guessed_letters:
                print(f"You already guessed '{guess}'. Try a different letter.")
                continue

            self.guessed_letters.append(guess)

            if guess in self.word:
                print(f"Good guess! '{guess}' is in the word.")
                # Reveal the guessed letter
                for index, letter in enumerate(self.word):
                    if letter == guess:
                        self.guessed_word[index] = guess
            else:
                print(f"Wrong guess! '{guess}' is not in the word.")
                self.lives -= 1

            if "_" not in self.guessed_word:
                print("\nCongratulations! You guessed the word:", self.word)
                break
        else:
            print("\nGame Over! You've run out of lives.")
            print("The word was:", self.word)

if __name__ == "__main__":
    hangman = Hangman()
    hangman.play()
