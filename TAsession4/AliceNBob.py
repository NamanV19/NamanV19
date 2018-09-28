def alice_n_bob(no_stones):      # receives number of stones
    i = 0
    turn = ""
    while i < no_stones:
        turn = "Alice"           # Alice's turn
        no_stones = no_stones-2
        turn = "Bob"             # Bob's turn
        no_stones = no_stones-2
    if no_stones % 2 == 0:       # checks if number of stones left is odd or even; to decide who is the winner
        print("Bob wins")
    else:
        print("Alice wins")


turn = ""
N = int(input("Please input number of stones"))  # decides the number of stones to play with
alice_n_bob(N)