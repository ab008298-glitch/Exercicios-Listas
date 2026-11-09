print("Programa para contar vogais, consoantes e outros caracteres")

frase = input("Digite uma frase: ")

vogais = 0
consoantes = 0
outros = 0

for letra in frase.lower():
    if letra in "aeiou":
        vogais += 1
    elif letra in "bcdfghjklmnpqrstvwxyz":
        consoantes += 1
    else:
        outros += 1

print("Quantidade de vogais:", vogais)
print("Quantidade de consoantes:", consoantes)
print("Quantidade de outros caracteres:", outros)