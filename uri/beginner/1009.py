[co1, ca1, pr1] = input().split(' ')
ca1 = int(ca1)
pr1 = float(pr1)
[co2, ca2, pr2] = input().split(' ')
ca2 = int(ca2)
pr2 = float(pr2)
to = ca1*pr1 + ca2 * pr2
print("VALOR A PAGAR: R$ %0.2f" % to)
