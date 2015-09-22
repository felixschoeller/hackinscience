import string

alph = string.ascii_lowercase
aaa = []

for letter in alph:
    for let in alph:
        if letter != let:
            aaa.append(letter + let)

for bbb in aaa:
    for ccc in aaa:
        if bbb != ccc:
            print(bbb + ccc)
