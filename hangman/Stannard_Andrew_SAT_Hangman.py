# Hangman with word spoken aloud
# Year 5 and Year 6 Spellings for SAT (Standard Assessment Tests)
# Andrew Stannard
# May 2022
# 


# Import external modules

import random
import string
from gtts import gTTS
from io import BytesIO
from mpg123 import Mpg123, Out123

# Open word list file to read using iteration
with open('word_list_SAT.txt','r') as fh:
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
    
# A function to say the selected word aloud

def say_word(selected_word):
    """Speaks the selected word out loud
    
    selected_word : string
    """
    # get audio from server using Google Text-To-Speech gTTS
    tts = gTTS(text=selected_word)
    # convert to file like object
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    # Play audio
    mp3 = Mpg123()
    mp3.feed(fp.read())

    out = Out123()
    for frame in mp3.iter_frames(out.start):
        out.play(frame)


# Setup the game variables for playing

# How many wrong attempts at guessing a letter have there been
attempts = 0

# Create Set of all the possible guesses
remaining_letters = set(string.ascii_lowercase)

# A list of all the incorrect guesses
wrong_letters = []

# Select word from list at random
selected_word = random.choice(words)

# Say word
say_word(selected_word)

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

