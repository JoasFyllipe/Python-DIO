texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#Utilizando um iterável
for letra in texto:
    if (letra.upper() in VOGAIS):
        print(letra, end="")
else:
    print()
    print("Executa no final do laço")