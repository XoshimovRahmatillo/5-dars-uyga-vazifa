def ikkilik_tub(n):
    if n<0:
        return "Error"
    return bin(n)[2:]

n=int(input("Sonni kiriting: "))
print(ikkilik_tub(n))