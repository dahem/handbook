import math
dic = {}

for x in range(1, 27):
    num_parts = math.ceil(x / 3)
    num_points = x % 3
    if num_points == 0:
        num_points = 3

    mask = " ".join(['.' * num_points for x in range(num_parts)])
    dic[mask] = chr(ord('a')+(x-1))


def run():
    n = int(input())

    for x in range(n):
        cad = input()
        print(dic[cad])


while True:
    try:
        run()
    except:
        break
