def check_if_vowel(character, list1):
    for item in list1:
        if character in list1:
            return True
        return False


char = 'z'
list2 = ["a", "e", "i", "o", "u"]
print(check_if_vowel(char, list2))

