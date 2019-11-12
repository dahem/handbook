n = int(input())
c = 0
r = 0
s = 0
for x in range(n):
    [a, b] = input().split()
    a = int(a)
    if b == 'C':
        c += a
    if b == 'R':
        r += a
    if b == 'S':
        s += a
tot = c + r + s
print("Total: %d cobaias" % tot)
print("Total de coelhos: %d" % c)
print("Total de ratos: %d" % r)
print("Total de sapos: %d" % s)
cc = float(c) * 100.0 / float(tot)
rr = float(r) * 100.0 / float(tot)
ss = float(s) * 100.0 / float(tot)
print("Percentual de coelhos: %.2f" % cc, '%')
print("Percentual de ratos: %.2f" % rr, '%')
print("Percentual de sapos: %.2f" % ss, '%')
