n = float(input())


if (n < 0 or n > 100):
    print("Fora de intervalo")
    exit()

if (n >= 0 and n <= 25):
    print("Intervalo [0,25]")
    exit()

if (n > 25 and n <= 50):
    print("Intervalo (25,50]")
    exit()
if (n > 50 and n <= 75):
    print("Intervalo (50,75]")
    exit()

if (n > 75 and n <= 100):
    print("Intervalo (75,100]")
    exit()
