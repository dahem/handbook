def run():
    n, m = map(int, input().split())
    if n == m == 0:
        raise Exception()
    print(n+m)


while True:
    try:
        run()
    except:
        break
