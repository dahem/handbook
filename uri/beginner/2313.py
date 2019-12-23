arr = [int(x) for x in input().split()]
arr.sort()
[a, b, c] = arr

if a + b > c:
    cad = "Valido"
    if a == b == c:
        cad += "-Equilatero"
    else:
        if a == b or b == c or c == a:
            cad += "-Isoceles"
        else:
            cad += "-Escaleno"
    print(cad)
    if a*a + b*b == c*c:
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")
