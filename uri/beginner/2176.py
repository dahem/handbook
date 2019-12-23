n = input()

if sum([int(x) for x in n]) % 2 == 0:
    print(n+'0')
else:
    print(n+'1')
