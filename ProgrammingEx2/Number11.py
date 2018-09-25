import string


def is_pangram(sentence):
    alphabet = string.ascii_letters

    for letter in alphabet:
        if letter in sentence:
            print(True)
            break
        else:
            print(False)
            break

x = 'z'
is_pangram(x)

