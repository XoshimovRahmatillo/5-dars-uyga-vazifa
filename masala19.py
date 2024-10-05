l=list(map(int,input("Sonlarni kiriting: ").split()))
juft=list(filter(lambda a:a%2==0,l))
toq=list(filter(lambda a:a%2==1,l))
print(f"Juft sonlar: {juft}\nTOq sonlar: {toq}")