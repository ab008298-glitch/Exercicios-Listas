print("Solicita idade de 7 pessoas e mostra quem tem 18 anos ou mais")
print()

nomes = []
idades = []

for i in range(7):
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    nomes.append(nome)
    idades.append(idade)

print("Pessoas com 18 anos ou mais: ")
for i in range(len(nomes)):
    if idades [i] >= 18:
        print(nomes[i])
