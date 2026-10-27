print("Programa para solicitar 11 valores e salvar em um vetor")
print()

valores = [""] * 11

for i in range(11):
    valores [i] = input (f"Digite o valor {i + 1}: ")

print("Valores informados: ")
for i in range(len(valores)):
    print(valores[i])
    if i < len(valores) - 1:
        print("-----------------------")
