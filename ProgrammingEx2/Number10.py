def find_longest_word(list1):
    list2 = []
    for items in list1:
        list2.append(len(items))
    max = list2[0]
    min = list2[0]
    size = len(list2)
    for i in range(size):
        if list2[i] > max:
            max = list2[i]
    print(max)


a = ["Baboon", "Tiger", "Anaconda"]
find_longest_word(a)