nome = "Joás"
idade = 19
profissao = "Programador"
linguagem = "Python"
saldo = 56.694

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e "
      f"estou matriculado no curso de {linguagem}.")


#Formatacao de valores

PI = 3.14159

print(f"Valor de PI: {PI: .2f}")# Se indica que quer 2 numeros depois do ponto, e não quer nenhum espaço antes do numero

print(f"Valor de PI: {PI: 10.2f}")# o numero antes do ponto indica a qnt de espaço antes do numero

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo: 5.2f}")