
s = set()
while True:
    try:
        cad = input()
        s.add(cad)
    except:
        break

print(len(s))
