def run(x, y, a, b):
    if a == x or b == y:
        return "divisa"
    if a > x and b > y:
        return "NE"
    if a < x and b > y:
        return "NO"
    if a < x and b < y:
        return "SO"
    if a > x and b < y:
        return "SE"


while True:
    n = int(input())
    if n == 0:
        break
    x, y = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        print(run(x, y, a, b))
