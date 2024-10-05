def f(a,b,c):
    if a+b==c:
        return 1
    else:
        return 0

a,b,c=map(int,input("SOnlarni kiriting: ").split())
print(f(a,b,c))