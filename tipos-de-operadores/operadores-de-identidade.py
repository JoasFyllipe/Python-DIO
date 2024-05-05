#Informa se ocupam o mesmo local de memoria

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso

curso is not nome_curso

saldo is limite


#Exemplo
saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)