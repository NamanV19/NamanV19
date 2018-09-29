def pascal(row, pascal_list):
    for i in range(row):
        print(pascal_list)
        pascal_new_list = []
        pascal_new_list.append(pascal_list[0])
        for i in range(len(pascal_list)-1):
            pascal_new_list.append(pascal_list[i]+pascal_list[i+1])
        pascal_new_list.append(pascal_list[-1])
        pascal_list = pascal_new_list


input_row = int(input("Please enter a number"))
list1 = [1]
pascal(input_row, list1)
