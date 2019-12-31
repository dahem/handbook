querty = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"


def run():
    s = input()
    ans = ""
    for x in s:
        if x == ' ':
            ans += ' '
        else:
            ans += querty[querty.index(x) - 1]
    print(ans)


while True:
    try:
        run()
    except:
        break
