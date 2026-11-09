print("Programa para contar quantas vezes um número aparece em uma lista")

numeros = []

for i in range(10):
    n = int(input("Digite um número: "))
    numeros.append(n)

x = int(input("Digite o número X: "))

quantidade = numeros.count(x)

print("O número", x, "aparece", quantidade, "vezes.")