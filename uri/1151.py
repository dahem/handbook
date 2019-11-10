a = int(input())
d = [0, 1, 1]
for i in range(3, a):
    d.append(0)
    d[i] = d[i-1] + d[i-2]

print(' '.join(map(str, d)))
