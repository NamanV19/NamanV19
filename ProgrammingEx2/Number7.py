def generate_n_chars(n, c):
    f = 0
    while f <= n:
        character = n*c
        f = f+1
    return character


print(generate_n_chars(5, "b"))

