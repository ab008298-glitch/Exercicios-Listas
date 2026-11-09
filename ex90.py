print("Programa para contar quantas vezes X aparece em 32 números")

x = int(input("Digite o número X: "))

numeros = []

for i in range(32):
    n = int(input("Digite um número: "))
    numeros.append(n)

quantidade = numeros.count(x)

print("O número", x, "apareceu", quantidade, "vezes.")