def convert_string_integer(list1, list2):
    for items in list1:
        list2.append(len(items))
    print (list2)
a = ["Baboon", "Tiger", "Anaconda"]
b = []
convert_string_integer(a, b)