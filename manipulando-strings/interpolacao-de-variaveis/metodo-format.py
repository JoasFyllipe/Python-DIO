nome = "Joás"
idade = 19
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Joás", "idade": 28}

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e"
     " estou matriculado no curso de {}".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e"
     " estou matriculado no curso de {0}".format(linguagem, profissao, idade, nome))
# os números entre as chaves indicam a posicao da variável
# iniciando do 0 sendo a primeira variável dentro do metodo.

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e"
     " estou matriculado no curso de {linguagem}".format(linguagem=linguagem, profissao=profissao, idade=idade, nome=nome))

print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(idade=idade, nome=nome))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))