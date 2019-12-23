def run():
    n, m = map(int, input().split())
    sol = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a == m and b == 0:
            sol += 1
    print(sol)


while True:
    try:
        run()
    except:
        break
