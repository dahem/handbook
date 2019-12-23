present, deadline = map(int, input().split())
if deadline < present:
    print("Eu odeio a professora!")
    exit()

if present + 3 <= deadline:
    print("Muito bem! Apresenta antes do Natal!")
    exit()

print("Parece o trabalho do meu filho!")

if present + 2 < 24:
    print("TCC Apresentado!")
else:
    print("Fail! Entao eh nataaaaal!")
