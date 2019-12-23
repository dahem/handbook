n = int(input())
suma = 0.0
dic = {
    1001: 1.5,
    1002: 2.5,
    1003: 3.5,
    1004: 4.5,
    1005: 5.5
}
for x in range(n):
    [a, b] = input().split()
    b = float(b)
    suma += dic[int(a)] * b

print("%.2f" % suma)
