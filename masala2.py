def zero(lst):
    zero_count = lst.count(0)

    non_zeros = [x for x in lst if x != 0]
    

    return non_zeros + [0] * zero_count


asl_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]


result = zero(asl_list)


print("Asl List:", asl_list)
print("Barcha nol ko'rsatilgan List:", result)
