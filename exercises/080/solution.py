import string

alph = string.ascii_lowercase
alpha = []

for letter in alph:
    for let in alph:
        if letter != let:
            alpha.append(letter + let)

for toto in alpha:
    for totot in alpha:
        if totot != toto:
            print(alpha)
