import re


def check_word(a, b):
    if len(a) > len(b):
        return False
    if len(a) == len(b):
        return a == b
    arr = [m.end() for m in re.finditer(a, b)]
    # print(arr)
    if len(arr) > 0:
        for x in arr:
            if len(b) == x or str(b[x]).isupper():
                return True
        return False
    return False


# print(check_word("ClF3", "4P12Si7CNF12BLiClF312ON12H"))
# print(check_word("C3H5N3O9", "C3H5N3O9ClF3KH20"))

cases = int(input())
for cas in range(cases):
    if cas != 0:
        print("")
    n = int(input())
    danger = []
    for x in range(n):
        danger.append(input())
    m = int(input())
    for x in range(m):
        cad = input()
        found = False
        for y in danger:
            if check_word(y, cad):
                found = True
                break
        if found:
            print("Abortar")
        else:
            print("Prossiga")
