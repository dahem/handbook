import math
num = 0
caw = 0
while True:
    s = input()
    if s == "caw caw":
        caw += 1
        print(num)
        num = 0
        if caw == 3:
            exit()
    ss = s[::-1]
    for x in range(3):
        if ss[x] == '*':
            num += 2 ** x
