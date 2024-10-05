def sortlash(sonlar):
    son=set(sonlar)
    
    
    return list(son)

N = int(input("N sonini kiriting: "))
sonlar = list(map(int, input("Sonlarni kiriting: ").split()))

natija = sortlash(sonlar)
print("Natija:", natija)