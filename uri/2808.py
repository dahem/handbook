[a, b] = input().split()

p1 = [ord(a[0]) - ord('a'), int(a[1]) - 1]
p2 = [ord(b[0]) - ord('a'), int(b[1]) - 1]

# print(p1, p2)

X = [2, 1, -1, -2, -2, -1, 2, 1]
Y = [1, 2,  2, 1, -1, -2, -1, -2]

for i in range(8):
    if p1[0] + X[i] == p2[0] and p1[1] + Y[i] == p2[1]:
        print("VALIDO")
        exit()
print("INVALIDO")
