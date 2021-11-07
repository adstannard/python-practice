# JHub Coding Scheme (JCS) Module 3: Python
# Andrew Stannard
# January 2020
# https://gist.github.com/adstannard/6e34155d349e72bf04d4fece014bbc8c


# Import external modules

import random
import string

# Open word list file to read using iteration
with open('word_list.txt','r') as fh:
    words = [line.strip() for line in fh]

# A function to display the choosen word with a mask of asterisk

def generate_display_word(selected_word, indx):
    """Displays the secret word in format '*****' 
    until letters are guess correctly.
    
    selected_word : string
    indx : index 
    """
    # Build word with letters or masking characters
    display_word = " ".join([letter if indx[i] else "*" for i, letter in enumerate(selected_word)])
    return display_word.strip()

# A function to allow the player to guess a letter in the selected word

def guess_letter(remaining_letters):
    """Allows the player to guess a letter in the word
     checking against the lowercase ascii character.
     Returns the current letter guessed. 
     
     remaining_letters : list of remaining ascii_lowercase letters yet to be guessed 
     """
    # Ask the player to guess a letter in the word
    while True:
        current_letter = input("Please enter your next guess: ").lower()
        # Check input is valid letter to prevent error
        if current_letter not in remaining_letters:
            #print("{0} is not valid letter".format(current_letter))
            print(f"{current_letter} is not valid letter")
        # Return a valid input    
        else:
            remaining_letters.remove(current_letter)
            return current_letter
    
    
# Setup the game variables for playing

# How many wrong attempts at guessing a letter have there been
attempts = 0

# Create Set of all the possible guesses
remaining_letters = set(string.ascii_lowercase)

# A list of all the incorrect guesses
wrong_letters = []

# Select word from list at random
selected_word = random.choice(words)

# An index to mask letter not yet guessed using list comprehension
indx = [letter not in remaining_letters for letter in selected_word]

# Is the word correct boolean
correct = False

# Running the game of hangman

# Game loop continues until 7 wrong letter attempts or word is guessed correctly
while attempts < 7 and not correct:

    # Print list of previous wrong letter attempts
    print("Previous Guesses: {0}".format(" ".join(wrong_letters)))
    #Print the word with masking characters
    print("Word: {0}".format(generate_display_word(selected_word, indx)))

    # Ask for the current letter to check
    current_letter = guess_letter(remaining_letters)

    # Check for current letter in the selected word
    if current_letter in selected_word:
        # Correct guess
        print("{0} is in the word.".format(current_letter))

        # Show matching letter in word
        for i in range(len(selected_word)):
            if selected_word[i] == current_letter:
                indx[i] = True
    else:
        # Incorrect guess
        print(f"{current_letter} is not in the word.")

        # Make an attempt used
        attempts +=1
        wrong_letters.append(current_letter)

    # Is the word complete
    if False not in indx:
        correct = True

# Game over - show word
print(f"The word is {selected_word}")

# Display the winning message when work correctly guessed
if correct:
   print("Congratulations you win")
else:
    print("You lose")


# Briefing details

# The script must ONLY stop to either ask for the next guess or because the game has been won or lost (i.e. no menus or other user input).
# Asking the user to make her next guess must use the following text (case sensitive and a space after the colon are necessary (I think)): “Please enter your next guess: “
# The text printed before “Please enter your next guess: “ must END in the word to be guessed with the unknown letters starred out (i.e. hello would start as ***** and change into *e*** after ‘e’ was guessed). The string must not contain any other stars.
# The program must print either “congratulations you win” or “you lose” on exit (not case sensitive).
# When a game is played, a word must be picked randomly (from a uniform distribution) from the word_list.txt file.
# The word_list.txt file must be stored in the same path as your code and when you load the file don't include the path (i.e. "open('word_list.txt', ...)").
# If the user makes 7 wrong guesses then they lose the game.
