def run():
    n, m = map(int, input().split())
    if n == m == 0:
        raise Exception()
    arrA = [int(x) for x in input().split()]
    arrB = [int(x) for x in input().split()]
    a = set(arrA)
    b = set(arrB)
    if len(a) < len(b):
        print(len(a.difference(b)))
    else:
        print(len(b.difference(a)))


while True:
    try:
        run()
    except:
        break
