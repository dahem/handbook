fibo = [0, 1, 1]
for x in range(3, 100):
    fibo.append(0)
    fibo[x] = fibo[x-1] + fibo[x-2]

for x in range(int(input())):
    a = int(input())
    print("Fib(%d) = %d" % (a, fibo[a]))
