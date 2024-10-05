def f(char):
    unlilar = 'aeiou' 
    closest = None
    min_distance = float('inf')  

    for unli in unlilar:
        distance = abs(ord(char) - ord(unli))
        if distance < min_distance:
            min_distance = distance
            closest = unli
    return closest
char = input("Harfni kiriting: ")
print(f(char))