print("Programa para multiplicar os valores de duas listas")

X = []
Y = []

for i in range(8):
    n = int(input("Digite um valor para X: "))
    X.append(n)

for i in range(8):
    n = int(input("Digite um valor para Y: "))
    Y.append(n)

for i in range(8):
    resultado = X[i] * Y[i]
    print(X[i], "x", Y[i], "=", resultado)