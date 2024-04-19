import random
import tkinter as tk
from tkinter import messagebox

# ASCII art for hangman stages
H_PICS = ['''
  +---+
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
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']

# List of words for the hangman game
words = 'Tendulkar Dravid Kohli Dhoni Ganguly Sehwag Sharma Kumble Kapil Jadeja Ashwin Shastri Gambhir Pathan Yuvraj Karthik Raina Harbhajan Agarkar Zaheer Jadhav Ishant Chahal Srinath Chawla Agarwal Pant Kuldeep Kambli Umesh'.split()

def get_rand_word(word_list):
    """Returns a random word from the word list."""
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

def display_b(missed, correct, secret):
    """Updates the hangman stage, missed letters, and secret word display."""
    hangman_text.config(text=H_PICS[len(missed)], font=('Courier New', 24), padx=20, pady=20)
    missed_letters_label.config(text=f"Missed letters: {' '.join(missed)}", font=('Arial', 16))

    blanks = ' '.join([letter if letter.lower() in correct else '_' for letter in secret])
    secret_word_label.config(text=blanks, font=('Arial', 24))

    if '_' not in blanks:  # Check if there are no more underscores (all letters guessed)
        messagebox.showinfo('Congratulations!', 'You have guessed the word correctly!')
        if play_a():
            reset_game()
        else:
            root.destroy()

def get_guessed(event=None):
    """Handles user's guesses and updates game state."""
    global max_missed
    guess = guess_entry.get().lower()  # Convert input to lowercase

    if len(guess) != 1:
        messagebox.showwarning('Invalid Input', 'Please enter a single letter.')
    elif guess in missed_letters + correct_letters:
        messagebox.showwarning('Duplicate Guess', 'You have already guessed that letter. Choose again.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        messagebox.showwarning('Invalid Input', 'Please enter a LETTER.')
    else:
        if guess in secret_word.lower():  # Compare lowercase version of the secret word
            correct_letters.append(guess)
        else:
            missed_letters.append(guess)
            max_missed -= 1

        display_b(missed_letters, correct_letters, secret_word)
        guess_entry.delete(0, tk.END)  # Clear the input field

    if max_missed == 0:
        messagebox.showinfo('Game Over', f'You have run out of guesses!\nThe word was "{secret_word}"')
        if play_a():
            reset_game()
        else:
            root.destroy()

def play_a():
    """Asks if the player wants to play again."""
    return messagebox.askyesno('Play Again', 'Do you want to play again?')

def reset_game():
    """Resets the game for a new round."""
    global secret_word, correct_letters, missed_letters, max_missed
    secret_word = get_rand_word(words)
    correct_letters = []
    missed_letters = []
    max_missed = 5
    display_b(missed_letters, correct_letters, secret_word)

# Create the main window
root = tk.Tk()
root.title('Hangman Game')

# Create and pack GUI elements
hangman_text = tk.Label(root, text="", font=('Courier New', 24), padx=20, pady=20)
hangman_text.pack()

missed_letters_label = tk.Label(root, text="Missed letters: ", font=('Arial', 16))
missed_letters_label.pack()

secret_word_label = tk.Label(root, text="", font=('Arial', 24))
secret_word_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()
guess_entry.focus()

guess_button = tk.Button(root, text="Guess", command=get_guessed)
guess_button.pack()

reset_button = tk.Button(root, text="Play Again", command=reset_game)
reset_button.pack()

# Initialize game variables
max_missed = 5
secret_word = get_rand_word(words)
correct_letters = []
missed_letters = []

# Display initial game state
display_b(missed_letters, correct_letters, secret_word)

# Bind Enter key to the guess function
root.bind('<Return>', get_guessed)

# Start the main event loop
root.mainloop()
