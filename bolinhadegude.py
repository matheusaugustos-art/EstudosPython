altura = int(input("Digite sua altura: "))
peso = int(input("Digite seu peso: "))

if altura >= 175 and altura <= 180:
    a = True
else:
    a = False


if peso >= 70 and peso <= 80:
    p = True
else:
    p = False 


if a == True and p == True:
    print("Aceito")
elif a == False and p == True:
    print("Recusado por altura")
elif a == True and p == False:
    print("Recusado por peso")
elif a == False and p == False:
    print("Totalmente recusado")