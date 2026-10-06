print(f"{' Caixa Eletrônico ':*^50}")

saldo = 1000
escolha =  saque = 0

while True:
    print('''Opçôes:
    [1] Ver saldo
    [2] Depositar
    [3] Sacar
    [4] Sair''')

    print('*' * 50)

    # se a escolha não for válida, cai no lop
    escolha = int(input('Escolha uma das opçôes: '))
    while not escolha in range(1, 5):
        print('Opção inválida!\n') 
        print('*' * 50)
        print('''Opçôes:
[1] Ver saldo
[2] Depositar
[3] Sacar
[4] Sair''')
        escolha = int(input('Escolha uma das opçôes: '))
    # determina conforme a escolha do usuário
    if escolha == 1:
        print(f'Seu saldo é de R$ {saldo:.2f}')
    elif escolha == 2:
        deposito = float(input('Quanto deseja depositar, sendo mais que 0: R$ '))
        # se o depósito for menor do 0 fica no loop até inserir um número maior do 0
        while deposito <= 0:
            print('Depósito inválido!, Tem que ser maior que 0!')
            deposito = float(input('Quanto deseja depositar, sendo mais que 0: R$ '))
        saldo += deposito
        print(f'Depósito de R$ {deposito:.2f} concluído, Saldo atual é de: R$ {saldo:.2f}')
        print('*' * 50)
    elif escolha == 3:
        saque = float(input('Quanto deseja sacar: R$ '))
        while saque > saldo or saque < 0:
            if saque > saldo:
                print(f'Saque maior do que o saldo atual R$ {saldo:.2f}')
            if saque <= 0:
                print('Saque menor ou igual a 0!')
            saque = float(input('Quanto deseja sacar: R$ '))
        saldo -= saque
        print(f'Saque de R$ {saque:.2f} concluído, Saldo atual {saldo:.2f}')
    elif escolha == 4:
        break

print(f'Saldo atual {saldo:.2f}')
