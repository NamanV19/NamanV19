def modul_42():
    list1 = []
    for i in range(0, 10):
        input_no = int(input("please enter a number"))  # input 10 numbers
        if input_no % 42 not in list1:  # if there is/are number(s) with same remainder in list, it will not be added
            list1.append(input_no % 42)
            x = (len(list1))  # calculates how many numbers are there with distinct remainder

    print(x)


modul_42()
