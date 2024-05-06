while True:
    numero = int(input("Informe um número: "))

    if (numero == 10):
        break #Encerra o laço

    if (numero %2 == 0):
        continue #Pula o que atende a condição

    print(numero)

