val = float(input())

tax = 0.0
if val >= 0 and val <= 2000:
    print('Isento')
    exit()

val -= 2000
tax += min(val, 1000) * 0.08
val -= 1000
if val <= 0:
    print("R$ %.2f" % tax)
    exit()
tax += min(val, 1500) * 0.18
val -= 1500
if val <= 0:
    print("R$ %.2f" % tax)
    exit()
tax += val * 0.28

print("R$ %.2f" % tax)
