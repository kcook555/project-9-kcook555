# Author: Kevin Phillips
# GitHub username: kcook555
# Date: 5/17/2025
# Description: Function that takes a string
#              and returns a dictionary of
#              letters and how many times they
#              appear in the string

def count_letters(input_string):
    """Return a dict of 'letter:letter count' for each letter in input_string."""
    letter_dict = {}
    for letter in input_string:
        #Use a set to search faster
        if letter.upper() in {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                              'W', 'X', 'Y', 'Z'}:
            if letter.upper() not in letter_dict:
                letter_dict[letter.upper()] = 1
            else:
                letter_dict[letter.upper()] += 1
    return letter_dict
