n = int(input())
a = b = 0
for i in range(n):
    a, b, c = map(int, input().split())
    flag = False
    if 200 <= a <= 300:
        if b >= 50:
            if c >= 150:
                flag = True
    if flag:
        print("Sim")
    else:
        print("Nao")
