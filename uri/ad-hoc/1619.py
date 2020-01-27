from datetime import datetime
cases = int(input())
for cas in range(cases):
    a, b = map(str, input().split())
    da = a.split('-')
    db = b.split('-')
    x = datetime(int(da[0]), int(da[1]), int(da[2]))
    y = datetime(int(db[0]), int(db[1]), int(db[2]))

    print(abs((y - x).days))
