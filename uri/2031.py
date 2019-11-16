n = int(input())
for x in range(n):
    a = input()
    b = input()

    if a == "pedra" == b:
        print("Sem ganhador")
        continue
    if a == "papel" == b:
        print("Ambos venceram")
        continue
    if a == "ataque" == b:
        print("Aniquilacao mutua")
        continue

    if a == "pedra":
        if b == "papel":
            print("Jogador 1 venceu")
            continue
        if b == "ataque":
            print("Jogador 2 venceu")
            continue
    if a == "papel":
        if b == "ataque":
            print("Jogador 2 venceu")
            continue
        if b == "pedra":
            print("Jogador 2 venceu")
            continue
    if a == "ataque":
        if b == "papel":
            print("Jogador 1 venceu")
            continue
        if b == "pedra":
            print("Jogador 1 venceu")
            continue
