def intersection(list1,list2):
    a=set(list1)
    b=set(list2)
    new=a.intersection(b)
    return list(new)

list1=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
list2=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(intersection(list1,list2))
    