import string

alph = string.ascii_lowercase

for letter in alph:
    for let in alph:
        if letter != let:
            print(letter + let)
