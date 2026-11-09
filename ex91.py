print("Programa para identificar números pares e ímpares")

numeros = []

for i in range(21):
    n = int(input("Digite um número inteiro: "))
    numeros.append(n)

impares = []

for n in numeros:
    if n % 2 != 0:
        impares.append(n)

if len(impares) == 0:
    print("Todos são pares.")
else:
    print("Existem números ímpares.")

    impares.sort()

    print("Números ímpares em ordem crescente:", impares)