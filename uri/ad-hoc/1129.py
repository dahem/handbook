def run():
    n = int(input())
    if n == 0:
        raise Exception()
    for x in range(n):
        arr = [int(x) <= 127 for x in input().split()]
        if arr.count(True) == 1:
            print(chr(arr.index(True) + ord('A')))
        else:
            print('*')


while True:
    try:
        run()
    except:
        break
