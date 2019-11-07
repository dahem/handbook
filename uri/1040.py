a, b, c, d = map(float, input().split())
m = a*2 + b*3 + c*4 + d*1
m /= 10
print("Media: %0.1f" % m)
if m < 5:
    print('Aluno reprovado.')
    exit()

if m >= 7:
    print('Aluno aprovado.')
    exit()

e = float(input())
print("Aluno em exame.")
print("Nota do exame: %0.1f" % e)
nm = (m + e) / 2
if m < 5:
    print('Aluno reprovado.')
    print("Media final: %0.1f" % nm)
    exit()
if m >= 5:
    print('Aluno aprovado.')
    print("Media final: %0.1f" % nm)
    exit()
