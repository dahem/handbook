def run():
    n = int(input())
    arr = [int(x) for x in input().split()]

    if sum(arr)/len(arr) >= 2.0/3.0:
        print("impeachment")
    else:
        print("acusacao arquivada")


while True:
    try:
        run()
    except:
        break
