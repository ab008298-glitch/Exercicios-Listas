print("Programa para calcular a média dos alunos")

nomes = []
notas = []

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota: "))

    nomes.append(nome)
    notas.append(nota)

media = sum(notas) / 5

print("A média da turma é:", media)

print("Alunos com nota menor que 7:")

for i in range(5):
    if notas[i] < 7:
        print(nomes[i], "-", notas[i])