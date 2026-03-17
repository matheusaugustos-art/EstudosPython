print("-----BEM VINDO-----")
idade = int(input("informe sua dade: "))
dc = (input("Você tem alguma doença crônica?: "))

if dc == "sim":
    q = int(input("Quantas?: "))
else:
    q = 0    

if idade >= 0 and idade <= 18:
    tb = 83.15
    ad = 0
elif idade >= 19 and idade <= 33:
    tb = 133.88
    ad = 0.05 * tb
elif idade > 33 and idade <= 44:
    tb = 203.73
    ad = 0.10 * tb
elif idade > 44 and idade <= 58:
    tb = 312.44
    ad = 0.15 * tb
elif idade > 58:
    tb = 498.53
    ad = 0.30 * tb
else:
    print("Idade inválida")
    exit()

total = tb + ad

print("Idade: ",idade)
print(q, "doenças crônicas")
print(f"O valor do seu plano ficou: R$ {total:.2f}")
