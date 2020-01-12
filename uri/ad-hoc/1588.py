
def score(e):
    return (-e["points"], -e["wins"], -e["gols"], e["ind"])


cases = int(input())

for cas in range(cases):
    arr = []
    n, m = map(int, input().split())
    for i in range(n):
        s = input()
        dic = {
            "name": s,
            "ind": i,
            "points": 0,
            "wins": 0,
            "gols": 0
        }
        arr.append(dic)
    for i in range(m):
        va, a, vb, b = map(str, input().split())
        va = int(va)
        vb = int(vb)
        for x in arr:
            if x['name'] == a:
                x["gols"] += va
                if va > vb:
                    x["wins"] += 1
                    x["points"] += 3
                elif va == vb:
                    x["points"] += 1

            if x['name'] == b:
                x["gols"] += vb
                if vb > va:
                    x["wins"] += 1
                    x["points"] += 3
                elif va == vb:
                    x["points"] += 1
    arr = sorted(arr, key=score)
    for x in arr:
        print(x["name"])
