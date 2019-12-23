n = int(input())
cases = int(input())
s = set()
for x in range(cases):
    s.add(int(input()))

print(n - len(s))
