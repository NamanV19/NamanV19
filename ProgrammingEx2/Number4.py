def reverse(Word):
    Palindrome = Word
    b = Palindrome[::-1]
    print(b)


InputWord = str(input("Please enter a word"))
reverse(InputWord)