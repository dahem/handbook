while True:
    n = int(input())
    if n == 0:
        break
    arr = [int(x) for x in input().split()]
    print("Mary won %d times and John won %d times" %
          (arr.count(0), arr.count(1)))
