def f(list1, list2):
    new_list = []
    max_length = max(len(list1), len(list2))

    for i in range(max_length):
        if i < len(list1):
            new_list.append(list1[i])
        if i < len(list2):
            new_list.append(list2[i])

    return new_list


list1 = [1, 2, 3]
list2 = [11, 22, 33]
print(f(list1, list2)) 

list1 = [1, 2, 3, 4, 5]
list2 = [11, 22, 33]
print(f(list1, list2))  

list1 = [1, 2]
list2 = [11, 22, 33, 44, 55]
print(f(list1, list2))  