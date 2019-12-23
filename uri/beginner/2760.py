a = input()
b = input()
c = input()


def cut(s):
    if len(s) < 10:
        return s
    return s[0:10]


print("%s%s%s" % (a, b, c))
print("%s%s%s" % (b, c, a))
print("%s%s%s" % (c, a, b))
print("%s%s%s" % (cut(a), cut(b), cut(c)))
