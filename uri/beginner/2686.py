def run():
    n = float(input())
    n %= 360
    sec = (24*60*60 * n) / 360.0
    sec = (int(sec) + 6*60*60) % (24*60*60)

    h = sec // (60*60)
    sec %= (60*60)
    m = sec // 60
    sec %= 60
    s = sec

    if 0 <= n < 90:
        print("Bom Dia!!")
    if 90 <= n < 180:
        print("Boa Tarde!!")
    if 180 <= n < 270:
        print("Boa Noite!!")
    if 270 <= n < 360:
        print("De Madrugada!!")
    print("%02d:%02d:%02d" % (h, m, s))


while True:
    try:
        run()
    except:
        break
