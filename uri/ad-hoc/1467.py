def run():
    a, b, c = map(int, input().split())
    if a == b == c:
        print('*')
        return
    if b == c != a:
        print('A')
    if a == c != b:
        print('B')

    if a == b != c:
        print('C')


while True:
    try:
        run()
    except:
        break
