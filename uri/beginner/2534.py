def run():
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    arr.sort(reverse=True)
    for i in range(m):
        y = int(input())
        print(arr[y-1])


while True:
    try:
        run()
    except:
        break
