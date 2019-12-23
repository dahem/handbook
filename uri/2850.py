

def run():
    x = input()
    if x == 'esquerda':
        print("ingles")
    elif x == 'direita':
        print("frances")
    elif x == 'nenhuma':
        print("portugues")
    else:
        print("caiu")


while True:
    try:
        run()
    except:
        break
