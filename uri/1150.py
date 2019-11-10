a = int(input())
while True:
    n = int(input())
    if n > a:
        suma = 0
        count = 0
        ind = a
        while suma < n:
            suma += ind
            count += 1
            ind += 1
        print(count)
        break
