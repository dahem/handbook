while True:
    n = int(input())
    if n == 0:
        break
    s = input()
    a = s.count('D')
    b = s.count('E')
    m = (a - b) % 4
    if m > 0:
        print("NLSO"[m])
    else:
        print("NOSL"[-m])
