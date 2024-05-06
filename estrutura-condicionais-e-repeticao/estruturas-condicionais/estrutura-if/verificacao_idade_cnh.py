MAIOR_IDADE = 18

idade = int(input("Digite a sua idade: "))

if(idade>=MAIOR_IDADE):
    print("Maior de idade, pode tirar a CNH.")
if(idade<MAIOR_IDADE):
    print("Idade não válida para tirar a CNH.")