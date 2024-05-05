saldo = 1000
saque = 200
limite = 100

saldo >= saque
saque <= limite

#Operador E
saldo >= saque and saque <= limite

#Operador OU
saldo >= saque or saque <= limite

#Operador de negacao

contatos_emergencia = []

not 1000 > 1500

not contatos_emergencia

not "saque 1500;"

not ""

#Exemplo

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >- saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)