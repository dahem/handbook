
n = int(input())
arr1 = [int(x) for x in input().split()]

dic = {}
dicRep = {}
ok = True
for x in arr1:
    if x not in dic.keys() or -x not in dic.keys():
        if x < 0:
            ok = False
            break
        dic[x] = 1
        dicRep[x] = 1
    else:
        if x > 0 and dic[x] > 0:
            ok = False
            break
        else:
            dic[x] = 1
            dicRep[x] += 1
            continue
        if x < 0 and dic[x] < 0:
            ok = False
            break
        else:
            dic[-x] = -1
            dicRep[-x] += 1
            continue

print(ok)
print(dic)
print(dicRep)
if not ok:
    print(-1)
    exit()
el = -1
mini = -100000000
for x in dic.keys():
    if dicRep[x] < mini:
        mini = dicRep[x]
        el = x
sol = 0
pos = []
for x in range(len(arr1)):
    if el == x:
        sol += 1
        pos.append(x)

print(sol)
sol.append(n)
for x in range(1, len(pos)):
    print(pos[x]-pos[x-1])
