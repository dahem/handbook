
n = int(input())
for i in range(n):
    b = int(input())
    s = input()
    sol = -10000
    acum = -10000
    for x in s:
        if x == 'P':
            acum += 1
            sol = max(acum, sol)
        else:
            sol = max(0, sol)
            acum = 0
    print(max(sol, 0))
