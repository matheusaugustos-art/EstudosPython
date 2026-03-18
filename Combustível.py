print("1 - Álcool - R$ 2,83/L")
print("2 - Gasolina - R$ 3,15/L")
print("-----BEM VINDO-----")
c = int(input("Qual combustível deseja abastecer? (dígite o código): "))
q = int(input("Quantos litros deseja?: "))

if c == 1:
    total = q * 2.83
elif c == 2:
    total = q * 3.15
else:
    print("Código inválido")

print("Total a pagar: ", total)        