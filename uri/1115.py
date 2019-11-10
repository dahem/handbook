while True:
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        print("primeiro")
        continue
    if a < 0 and b < 0:
        print("terceiro")
        continue
    if a > 0 and b < 0:
        print("quarto")
        continue
    if a < 0 and b > 0:
        print("segundo")
        continue
    break
