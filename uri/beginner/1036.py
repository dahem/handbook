a, b, c = map(float, input().split())

if(a == 0 or b*b - 4*a*c < 0):
    print("Impossivel calcular")
    exit()
x1 = (-b + (b*b - 4.0*a*c)**0.5)
x1 /= 2.0*a
x2 = (-b - (b*b - 4.0*a*c)**0.5)
x2 /= 2.0*a
print("R1 = %0.5f" % x1)
print("R2 = %0.5f" % x2)
