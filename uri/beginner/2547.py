def run():
    n, m, p = map(int, input().split())
    sol = 0
    for _ in range(n):
        x = int(input())
        if m <= x <= p:
            sol += 1
    print(sol)


while True:
    try:
        run()
    except:
        break
