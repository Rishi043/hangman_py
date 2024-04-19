# Importing necessary libraries
import random
import os

# ASCII art for hangman stages and a color class for terminal output
hangman = ['''   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

# List of cricketers' names for the hangman game
word_list = ["Tendulkar", "Dravid", "Kohli", "Dhoni", "Ganguly", "Sehwag",
             "Sharma", "Kumble", "Kapil", "Jadeja", "Ashwin", "Shastri",
             "Gambhir", "Pathan", "Yuvraj", "Karthik", "Raina", "Harbhajan",
             "Agarkar", "Zaheer", "Jadhav", "Ishant", "Chahal", "Srinath",
             "Chawla", "Agarwal", "Pant", "Kuldeep", "Kambli", "Umesh"]

# Choosing a random word from the word list
chosen_word = random.choice(word_list)

# Clearing the terminal screen
os.system("clear")

# Creating the alphabet list
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Printing the alphabet in underline using the color class
print(bcolors.UNDERLINE + f"{' '.join(alphabet)}\n" + bcolors.ENDC)

# Initializing variables for the game
screen = []
guessed = []
game_over = False
counter = 6

# Generating dashes for the secret word
for _ in range(len(chosen_word)):
    screen += "_"

# Printing the initial game state with dashes and the first hangman stage
print(bcolors.OKBLUE + f"\t\t{' '.join(screen)}" + bcolors.ENDC)
print(bcolors.OKCYAN + hangman[0] + bcolors.ENDC)

# Game loop until game_over is True
while not game_over:
    # Taking user input for guessing a word
    guess_a_word = input("\nGuess a letter: ").lower()

    # Clearing the terminal screen
    os.system("clear")

    # Handling duplicate guesses
    if guess_a_word in guessed:
        print(bcolors.FAIL + f"\t\tYou already guessed '{guess_a_word}'!" +  bcolors.ENDC)
    elif guess_a_word not in guessed:
        if guess_a_word not in chosen_word:
            counter -= 1
        guessed += guess_a_word

    # Updating the screen with guessed letters
    for point in range(len(chosen_word)):
        letter_in_word = chosen_word[point]
        if guess_a_word == letter_in_word:
            screen[point] = guess_a_word

    # Updating the alphabet with guessed letters
    if guess_a_word in alphabet:
        alphabet.remove(guess_a_word)

    # Printing the updated game state and hangman stages
    print(bcolors.OKBLUE + f"\t\t{' '.join(screen)}" + bcolors.ENDC)

    # Printing the appropriate hangman stage based on the number of incorrect guesses
    if counter >= 0 and counter < len(hangman):
        print(bcolors.OKCYAN + hangman[counter] + bcolors.ENDC)

    # Game over condition if all attempts are used
    if counter == 0:
        game_over = True
        print(bcolors.FAIL + f"\n\n-------YOU LOST!--------\n" + bcolors.ENDC)
        print(bcolors.FAIL + f"The answer was --->  " + bcolors.ENDC + bcolors.OKGREEN + f"{chosen_word}\n" + bcolors.ENDC)

    # Game over condition if all letters are guessed correctly
    if "_" not in screen:
        game_over = True
        print(bcolors.HEADER + "\n\nCongratulations!\nYOU WON THE GAME :)\n" + bcolors.ENDC)
