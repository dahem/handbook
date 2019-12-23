dic = {
    "suco de laranja": 120,
    "morango fresco": 85,
    "mamao": 85,
    "goiaba vermelha": 70,
    "manga": 56,
    "laranja": 50,
    "brocolis": 34,
}
while True:
    n = int(input())
    if n == 0:
        break
    can = 0
    for x in range(n):
        s = input().split()
        a = int(s[0])
        k = " ".join(s[1:])
        can += dic[k] * a
    if 110 <= can <= 130:
        print(can, "mg")
    else:
        if can > 130:
            print("Menos", can - 130, "mg")
        else:
            print("Mais", 110 - can, "mg")
