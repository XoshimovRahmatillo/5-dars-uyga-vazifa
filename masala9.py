def ochir(sonlar):
    takrorlanishlar = {}
    for son in sonlar:
        if son in takrorlanishlar:
            takrorlanishlar[son] += 1
        else:
            takrorlanishlar[son] = 1

    natija = [son for son in sonlar if takrorlanishlar[son] > 1]

    return natija

N = int(input("N sonini kiriting: "))
sonlar = list(map(int, input("Sonlarni kiriting: ").split()))

natija = ochir(sonlar)
print("Natija:", natija)
