partida = 0
vf = 0
vv = 0
e = 0

print("-----BEM VINDO-----")
print("1 - Sim")
print("2 - Não")
opcao = int(input(("Deseja revisar as últimas partidas?: ")))

while opcao == 1:

    partida += 1
    print("Dados da partida ", partida)

    f = input("Gols marcados pelo Flamengo: ")
    v = input("Gols marcados pelo Vasco: ")

    if f > v:
        print("Vitória do Flamengo")
        vf += 1
    elif v > f:
        print("Vitória da vasco")
        vv += 1
    else:
        print("Empate")
        e += 1     

    opcao = int(input("Deseja registrar outra partida? (1-Sim / 2-Não): "))

print("--- RESUMO DO DIA ---")
print("Total de partidas: ", partida)
print("Vitórias Flamengo: ", vf)
print("Vitórias Vasco: ", vv)
print("Empates: ", e)
