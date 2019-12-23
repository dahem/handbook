def run():
    n = int(input())
    n %= 360
    if 0 <= n < 90:
        print("Bom Dia!!")
    if 90 <= n < 180:
        print("Boa Tarde!!")
    if 180 <= n < 270:
        print("Boa Noite!!")
    if 270 <= n < 360:
        print("De Madrugada!!")


while True:
    try:
        run()
    except:
        break
