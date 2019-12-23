

def run():
    n = int(input())
    m, l = map(int, input().split())
    deck_m = []
    deck_l = []
    for x in range(m):
        arr = [int(x) for x in input().split()]
        deck_m.append(arr)
    for x in range(l):
        arr = [int(x) for x in input().split()]
        deck_l.append(arr)

    ind_m, ind_l = map(int, input().split())
    attr = int(input())
    if deck_m[ind_m - 1][attr - 1] > deck_l[ind_l - 1][attr - 1]:
        print("Marcos")
    elif deck_m[ind_m - 1][attr - 1] < deck_l[ind_l - 1][attr - 1]:
        print("Leonardo")
    else:
        print("Empate")


while True:
    try:
        run()
    except:
        break
