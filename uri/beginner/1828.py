n = int(input())
mat = [
    ["tesoura", "papel"],
    ["papel", "pedra"],
    ["pedra", "lagarto"],
    ["lagarto", "Spock"],
    ["Spock", "tesoura"],
    ["tesoura", "lagarto"],
    ["lagarto", "papel"],
    ["papel", "Spock"],
    ["Spock", "pedra"],
    ["pedra", "tesoura"]
]
for i in range(1, n+1):
    a, b = input().split()
    if a == b:
        print("Caso #%d: De novo!" % i)
        continue
    for x in mat:
        if x[0] == a and x[1] == b:
            print("Caso #%d: Bazinga!" % i)
            continue
    for x in mat:
        if x[0] == b and x[1] == a:
            print("Caso #%d: Raj trapaceou!" % i)
            continue
