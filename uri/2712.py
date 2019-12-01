import re

n = int(input())

for x in range(n):
    cad = input()
    if re.match("^[A-Z]{3}-[0-9]{4}$", cad):
        if cad[-1] == '1' or cad[-1] == '2':
            print("MONDAY")

        elif cad[-1] == '3' or cad[-1] == '4':
            print("TUESDAY")

        elif cad[-1] == '5' or cad[-1] == '6':
            print("WEDNESDAY")

        elif cad[-1] == '7' or cad[-1] == '8':
            print("THURSDAY")

        elif cad[-1] == '9' or cad[-1] == '0':
            print("FRIDAY")
    else:
        print("FAILURE")
