n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))
soma = 0

if n2 <= 0:
    print("Operação inválida, n2 tem que ser > 0!")
    n2 = int(input())

for i in range(n2):
    soma += (n1 + i)

print("Soma de", n1, "até", n2, "=", soma)