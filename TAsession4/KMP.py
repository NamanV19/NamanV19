def convert(scientists_names):
    data = scientists_names.split("-")  # converts string to list and "-" is omitted
    storing_initials = ""
    for i in data:  # for items in list
        storing_initials = storing_initials + i[0]  # initial letters of items are added
    print(storing_initials)


names_of_scientists = str(input("Please enter scientists name"))
convert(names_of_scientists)