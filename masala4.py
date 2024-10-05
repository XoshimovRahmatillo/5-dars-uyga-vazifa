def dublicat(lst):
    ls = []
    ls1 = set()

    for i in lst:
        i_tuple = tuple(i)
        if i_tuple not in ls1:
            ls1.add(i_tuple)
            ls.append(i)
    return ls

ls = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
result = dublicat(ls)
print(result)
