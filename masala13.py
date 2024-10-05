def f(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

n=int(input("N sonini kiriting: "))
print(f(n))