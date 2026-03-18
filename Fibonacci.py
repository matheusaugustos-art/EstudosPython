n1 = int(input("Quantos termpos deseja somar: "))
fibonacci = [1,1]
soma = 0
posicao = 2

while len (fibonacci) < n1:
    soma = fibonacci[posicao - 1] + fibonacci[posicao - 2]
    fibonacci.append(soma)
    posicao += 1

for i in fibonacci:
    print(i)

print("Soma total:", sum(fibonacci))