def to_minutes(h, m):
    return h * 60 + m


def run():
    h1, m1, h2, m2 = map(int, input().split())
    if h1 == m1 == h2 == m2 == 0:
        raise Exception()

    if h1 == m1 == h2 == m2:
        print(0)
        return

    isNextDay = h1 > h2 or (h1 == h2 and m1 > m2)
    if not isNextDay:
        print(to_minutes(h2, m2) - to_minutes(h1, m1))
    else:
        print(to_minutes(h2+24, m2) - to_minutes(h1, m1))


while True:
    try:
        run()
    except:
        break
