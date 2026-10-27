print("Recebe 18 números e coloca eles na ordem inversa")
print()

numeros = [""] * 18

for i in range(18):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

print("Numeros em ordem inversa: ")
for i in range(len(numeros) -1, -1, -1):
    print(numeros[i])
