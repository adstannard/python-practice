# Morse code: Text to Morse code
# Andrew Stannard
# May 2022
#!/usr/bin/env python3


# Morse Dictionary
morse_code = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
             'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 
             'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
             'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
             'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', 
             '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', 
             '9':'----.', '0':'-----', ',':'--..--', '.':'.-.-.-', '?':'..--..',
             ';':'-.-.-', ':':'---...', '/':'-..-.', '-':'-....-', "'":'.----.',
             '(':'-.--.', ')':'-.--.-', '_':'..--.-', '@':'.--.-.', '!':'-.-.--',
             '&':'.-...', '=':'-...-', '+':'.-.-.', '"' : '.-..-.', '$':'...-..-', ' ':'  '}

# Encode Morse function

def encode_morse(text):
    code = ''
    # Loop through each letter in the text
    for letter in text.upper():
        # Check if letter is in the dictionary
        if letter in morse_code:
            # If it is, add the morse code
            code += morse_code[letter] + ' '

    # Return the morse code
    return code

print(encode_morse('Hello my name is Andrew'))