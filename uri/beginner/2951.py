n, towin = map(int, input().split())
dic = {}
for x in range(n):
    s = input().split()
    dic[s[0]] = int(s[1])
m = int(input())
suma = sum([dic[x] for x in input().split()])
print(suma)
if suma >= towin:
    print("You shall pass!")
else:
    print("My precioooous")
