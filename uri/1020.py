n = int(input())

a = n // 365
n = n % 365
b = n // 30
n = n % 30
c = n

print("%d ano(s)" % a)

print("%d mes(es)" % b)

print("%d dia(s)" % c)
