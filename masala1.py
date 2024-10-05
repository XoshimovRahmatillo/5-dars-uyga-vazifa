ls = [1, 3, 5, 7, 9, 10]
ls1 = [2, 4, 6, 8]

def f(ls, val):
    ls_1 = ls[:-1]  
    full = ls_1 + [val]
    return full

ls2 = list(map(f, [ls] * len(ls1), ls1))
print(ls2)
