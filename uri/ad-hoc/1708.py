import math


def run():
    a, b = map(int, input().split())
    print(math.ceil(b/(b-a)))


while True:
    try:
        run()
    except:
        break
