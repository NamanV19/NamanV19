def overlapping(list1, list2):
    for item in list1:
        for item2 in list2:
            if item == item2:
                return True
            else:
                return False


a = [3, 5, 7, 8, 9]
b = [0, 2, 4, 6, 10]
print(overlapping(a, b))