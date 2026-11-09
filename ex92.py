print("Programa para encontrar valores comuns em duas listas")

vetor1 = []
vetor2 = []

for i in range(10):
    n = int(input("Digite um valor para o primeiro vetor: "))
    vetor1.append(n)

for i in range(12):
    n = int(input("Digite um valor para o segundo vetor: "))
    vetor2.append(n)

comuns = []

for n in vetor1:
    if n in vetor2 and n not in comuns:
        comuns.append(n)

comuns.sort(reverse=True)

print("Valores comuns aos dois vetores:", comuns)