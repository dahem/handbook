def run():
    cad = input()
    n = int(input())
    print("".join([cad[int(x)-1] for x in input().split()]))


while True:
    try:
        run()
    except:
        break
