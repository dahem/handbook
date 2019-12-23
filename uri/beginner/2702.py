
n, m, p = map(int, input().split())

n1, m1, p1 = map(int, input().split())
sol = 0
if n < n1:
    sol += n1 - n

if m < m1:
    sol += m1 - m


if p < p1:
    sol += p1 - p
print(sol)
