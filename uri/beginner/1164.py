
n = int(input())
for x in range(n):
    a = int(input())
    suma = 0
    i = 1
    while i*i <= a:
        if a % i == 0:
            j = a / i
            if i != j:
                suma += i
                suma += j
            else:
                suma += i
        i += 1
    if suma == 2 * a:
        print(a, "eh perfeito")
    else:
        print(a, "nao eh perfeito")
