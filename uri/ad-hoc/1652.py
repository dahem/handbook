
n, m = map(int, input().split())

dic = {}

for x in range(n):
    a, b = map(str, input().split())
    dic[a] = b

for x in range(m):
    s = input()
    if s in dic:
        print(dic[s])
    else:
        if s[-1] == 'y' and s[-2] not in ['a', 'e', 'i', 'o', 'u']:
            print(s[:-1] + 'ies')
            continue
        if s[-1] in ['o', 's', 'x'] or s.endswith('ch') or s.endswith('sh'):
            print(s+'es')
            continue
        print(s+'s')
