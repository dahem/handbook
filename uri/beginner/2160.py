ind = 1
size = 0
while True:
    try:
        line = input()
        size += len(line)
    except:
        if size <= 80:
            print("YES")
        else:
            print("NO")
        break
