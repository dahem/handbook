cases = int(input())


def run(i, mov, pas):
    if pas[i] == -1:
        return mov[i]
    return run(pas[i], mov, pas)


for cas in range(cases):
    n = int(input())
    mov = [0 for x in range(n)]
    pas = [-1 for x in range(n)]
    pos = 0

    for x in range(n):
        act = input()
        if act == 'LEFT':
            mov[x] = -1
            pos -= 1

        elif act == 'RIGHT':
            mov[x] = 1
            pos += 1

        else:
            pas[x] = int(act.split()[-1]) - 1
            pos += run(pas[x], mov, pas)

    print(pos)
