n1 = int(input("Dígtie n1: "))
n2 = int(input("Dígtie n2: "))

while n1 != n2:
    if n1 > n2:
        n1 = n1 - n2
    else:
        n2 = n2 - n1

print(n1)        
