print("Programa para inserir um separador entre os caracteres de uma frase")

frase = input("Digite uma frase: ")
separador = input("Digite o separador: ")

resultado = separador.join(frase)

print("Frase com separador:")
print(resultado)