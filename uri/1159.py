while True:
    x = int(input())
    if x == 0:
        break
    suma = 0
    count = 0
    while(count < 5):
        if x % 2 == 0:
            count += 1
            suma += x
        x += 1
    print(suma)
