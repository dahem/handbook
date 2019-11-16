n = int(input())
asum = 0
apos = 0
bsum = 0
bpos = 0
csum = 0
cpos = 0
for x in range(n):
    input()
    a, b, c = map(int, input().split())
    asum += a
    bsum += b
    csum += c
    ap, bp, cp = map(int, input().split())
    apos += ap
    bpos += bp
    cpos += cp

print("Pontos de Saque: %.2f %%." % (apos*100.0/asum))
print("Pontos de Bloqueio: %.2f %%." % (bpos*100.0/bsum))
print("Pontos de Ataque: %.2f %%." % (cpos*100.0/csum))
