print("Algoritmo que solicita 12 números e mostra os pares e ímpares")
print()

numeros = []

for i in range(12):
    numero = int(input(f"Informe o número {i + 1}: "))
    numeros.append(numero)

print("Números pares: ")
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(numeros[i])

print("Números ímpares: ")
for i in range(len(numeros)):
    if numeros[i] % 2 != 0:
        print(numeros[i])
