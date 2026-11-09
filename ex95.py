print("Programa para trocar as posições dos caracteres de uma lista")

caracteres = []

for i in range(12):
    letra = input("Digite um caractere: ")
    caracteres.append(letra)

for i in range(0, 12, 2):
    caracteres[i], caracteres[i+1] = caracteres[i+1], caracteres[i]

print("Resultado após as trocas:")
print(caracteres)