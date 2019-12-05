def by_day(date):
    day, month, year = map(int, date.split('/'))
    return day + month * 12 + year * 365


def run():
    n, m = map(int, input().split())
    sol = []
    for i in range(m):
        arr = input().split()
        pos = [int(x) for x in arr[1:]]
        if sum(pos) == n:
            sol.append(arr[0])
    sol.sort(key=by_day)

    if len(sol) == 0:
        print("Pizza antes de FdI")
    else:
        print(sol[0])


while True:
    try:
        run()
    except:
        break
