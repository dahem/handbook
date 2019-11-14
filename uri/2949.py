n = int(input())
dic = {
    'A': 0,
    'E': 0,
    'H': 0,
    'M': 0,
    'X': 0,
}
for x in range(n):
    s = input().split()
    dic[s[1]] += 1

print(dic['X'], "Hobbit(s)")
print(dic['H'], "Humano(s)")
print(dic['E'], "Elfo(s)")
print(dic['A'], "Anao(s)")
print(dic['M'], "Mago(s)")
