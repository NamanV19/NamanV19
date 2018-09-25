def make_ing_form(end_e, end_ie, cvc, dflt):
    answer = " "
    if end_e[-1] == "e":
        answer = end_e + "ing"
        print(answer)
    else:
        print("you are wrong")
    if end_ie[-2:] == "ie":
        answer2 = end_ie[0:-2:] + "ying"
        print(answer2)
    else:
        print("you are wrong")
    vowels = ["a", "e", "i", "o", "u"]
    if cvc[1] in vowels and len(cvc) == 3:
        cvc = cvc + cvc[2] + "ing"
        print(cvc)
    else:
        print("you are wrong")
    dflt = dflt+"ing"
    print(dflt)


make_ing_form("see", "lie", "bob", "cnn")