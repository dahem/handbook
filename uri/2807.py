x = int(input())
arr = [0] * 40
arr[0] = 1
arr[1] = 1

for i in range(2, 40):
    arr[i] = arr[i-1] + arr[i-2]

r_arr = arr[0:x][::-1]
print(" ".join(map(str, r_arr)))
