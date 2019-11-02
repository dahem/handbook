pi = 3.14159

a, b, c = map(float, input().split())


print("TRIANGULO: %0.3f" % (a*c/2.0))
print("CIRCULO: %0.3f" % (pi * c*c))
print("TRAPEZIO: %0.3f" % (min(a, b)*c + (max(a, b) - min(a, b))*c/2.0))
print("QUADRADO: %0.3f" % (b*b))
print("RETANGULO: %0.3f" % (a*b))
