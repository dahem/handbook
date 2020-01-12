n = int(input())
for i in range(n):
    ans1 = 0
    for j in range(3):
        x, d = map(int, input().split())
        ans1 += x*d
    ans2 = 0
    for j in range(3):
        x, d = map(int, input().split())
        ans2 += x*d
    if ans1 > ans2:
        print("JOAO")
    else:
        print("MARIA")
