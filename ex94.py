print("Programa para substituir caracteres especiais por traços")

frase = input("Digite uma frase: ")

nova_frase = ""

for letra in frase:
    if letra in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        nova_frase += letra
    else:
        nova_frase += "-"

print("Frase modificada:", nova_frase)