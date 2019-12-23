n = int(input())
ind = 1
for x in range(n):
    for y in range(4):
        if ind % 4 == 0:
            print("PUM")
        else:
            print(ind, end=" ")
        ind += 1
