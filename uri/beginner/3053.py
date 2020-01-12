def get_ind(s):
    return ord(s) - ord('A')


n = int(input())
start = input()

arr = [0, 0, 0]
arr[get_ind(start)] = 1
for i in range(n):
    mov = input()
    if mov == '1':
        arr[0], arr[1] = arr[1], arr[0]
    if mov == '2':
        arr[1], arr[2] = arr[2], arr[1]
    if mov == '3':
        arr[0], arr[2] = arr[2], arr[0]


for i in range(3):
    if arr[i] == 1:
        print(chr(i+ord('A')))
        break
