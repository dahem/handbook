n = int(input())

map_power = {
    'fire': {
        'damage': 200,
        '1': 20,
        '2': 30,
        '3': 50
    },
    'water': {
        'damage': 300,
        '1': 10,
        '2': 25,
        '3': 40
    },
    'earth': {
        'damage': 400,
        '1': 25,
        '2': 55,
        '3': 70
    },
    'air': {
        'damage': 100,
        '1': 18,
        '2': 38,
        '3': 60
    }
}


def distance(x1, y1, x2, y2):
    return ((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2)) ** 0.5


for x in range(n):
    w, h, x1, y1 = map(float, input().split())
    [magic, level, x2, y2] = input().split()
    x2 = float(x2)
    y2 = float(y2)

    damage = map_power[magic]['damage']
    radius = float(map_power[magic][level])

    if (x1 < x2 < x1 + w) and (y1 < y2 < y1 + h):
        print(damage)
        continue

    if distance(x1, y1, x2, y2) <= radius:
        print(damage)
    elif distance(x1+w, y1, x2, y2) <= radius:
        print(damage)
    elif distance(x1, y1+h, x2, y2) <= radius:
        print(damage)
    elif distance(x1+w, y1+h, x2, y2) <= radius:
        print(damage)
    else:
        if x1 < x2 < x1 + w and distance(x2, y1, x2, y2) <= radius:
            print(damage)
        elif x1 < x2 < x1 + w and distance(x2, y1+h, x2, y2) <= radius:
            print(damage)
        elif y1 < y2 < y1 + h and distance(x1, y2, x2, y2) <= radius:
            print(damage)
        elif y1 < y2 < y1 + h and distance(x1+w, y2, x2, y2) <= radius:
            print(damage)
        else:
            print(0)
