a = 0
b = 0
while True:
    cad = input()

    if cad == 'ABEND':
        break
    [n, m] = cad.split()
    m = int(m)
    if n == 'SALIDA':
        a += m
        b += 1
    else:
        a -= m
        b -= 1
print(a)
print(b)
