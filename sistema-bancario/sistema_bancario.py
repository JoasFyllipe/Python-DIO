menu = ''' 
    [1] Deposito
    [2] Saque
    [3] Extrato
    [0] Sair

=> '''

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

senha1 = input("Crie uma senha: ") #Solicita que o cliente crie uma senha para acessar.

while (True):

    opcao = (int(input(menu)))

    if (opcao == 1):
        valor = float(input("Digite o valor a ser depositado: "))
        
        if(valor > 0):
            saldo += valor
            extrato += (f"Depósito: R$ {valor:.2f}\n")

        else:
            print("Deposito não realizado, digite um valor válido!")

    elif (opcao == 2):
        valor = float(input("Digite o valor a ser sacado: "))

        senha2 = input("Digite sua senha novamente: ")#Solicita a senha para realizar o saque

        if(senha1 == senha2):

            excedeu_saldo = (valor > saldo)

            excedeu_limite = (valor > limite)

            excedeu_saques = (valor >= LIMITE_SAQUES)

            if(excedeu_saldo):
                print("Operação não realizada! Você não tem saldo suficiente.")
        
            elif(excedeu_limite):
                print("Operação não realizada! O valor do saque excede o limite.")
        
            elif(valor > 0):
                saldo -= valor
                extrato += (f"Saque: R$: {valor: .2f}")
                numero_saques += 1
                print("Saque realizado com sucesso!")
        
            else:
                print("Operação não realizada, o valor informado é inválido.")
    
        else: 
            print("Senha Incorreta! verifique e digite novamante.")

    elif(opcao == 3):
        print("\n=============== EXTRATO ===============\n")
        print("Não foram realizadas movimentações." if (not extrato) else(extrato))
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("\n=======================================\n")

    elif(opcao == 0):
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")