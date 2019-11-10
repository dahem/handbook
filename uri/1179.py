par = []
impar = []
for x in range(15):
    a = int(input())
    if a % 2 == 0:
        par.append(a)
        if len(par) == 5:
            for i in range(len(par)):
                print("par[%d] = %d" % (i, par[i]))
            par = []
    else:
        impar.append(a)
        if len(impar) == 5:
            for i in range(len(impar)):
                print("impar[%d] = %d" % (i, impar[i]))
            impar = []


for i in range(len(impar)):
    print("impar[%d] = %d" % (i, impar[i]))

for i in range(len(par)):
    print("par[%d] = %d" % (i, par[i]))
