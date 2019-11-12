arr = [int(x) for x in input().split()]
suma = 0
for x in range(arr[0], arr[0]+arr[-1]):
    suma += x
print(suma)
