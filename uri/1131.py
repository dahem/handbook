g = 0
i = 0
e = 0
a, b = map(int, input().split())
if a > b:
    i += 1
elif a == b:
    e += 1
else:
    g += 1
num = 1
while True:
    ask = input()
    print("Novo grenal (1-sim 2-nao)")
    if ask == '2':
        print("%d grenais" % num)
        print("Inter:%d" % i)
        print("Gremio:%d" % g)
        print("Empates:%d" % e)
        if i > g:
            print("Inter venceu mais")
        elif i == g:
            print("Não houve vencedor")
        else:
            print("Gremio venceu mais")
        break
    else:
        a, b = map(int, input().split())
        num += 1
        if a > b:
            i += 1
        elif a == b:
            e += 1
        else:
            g += 1
