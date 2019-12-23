def win_a(arr):
    [a, b, c] = arr
    if b != c:
        return False
    if a == "papel":
        return b == "pedra"
    if a == "tesoura":
        return b == "papel"
    if a == "pedra":
        return b == "tesoura"
    return False


while True:
    try:
        [a, b, c] = input().split()
        if win_a([a, b, c]):
            print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
        elif win_a([b, a, c]):
            print("Iron Maiden's gonna get you, no matter how far!")
        elif win_a([c, a, b]):
            print("Urano perdeu algo muito precioso...")
        else:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
    except:
        break
