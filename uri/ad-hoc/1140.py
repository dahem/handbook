def check(s):
    d = s.split(' ')
    for x in d:
        if x[0].lower() != d[0][0].lower():
            return False
    return True


while True:
    s = input()
    if s == '*':
        break
    if check(s):
        print("Y")
    else:
        print("N")
