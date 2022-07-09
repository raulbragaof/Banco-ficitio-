import os
import time
from random import randint

abrir_conta = input("Abrir conta no Bradesk?: ")
if abrir_conta.upper() == 'S':
    print("Vamos pedir alguns dados, ok?")
    time.sleep(0.9)

    os.system("clear")

    nome_client = input("Nome: ")
    idade_client = input("Idade: ")
    if idade_client.isnumeric():
        idade_client = int(idade_client)
        if idade_client > 18:
            agencia = 144
            conta_random = randint(4345, 5660)
            print('Conta corrente foi aberta. Segue os dados')
            time.sleep(0.9)
            os.system('clear')
            print(
                f'-=-=-=-=[ Dados bancarios ]-=-=-=-=-\n\n'
                f'Nome: {nome_client.upper()}\n'
                f'Agencia: {agencia}\n'
                f'Conta: {conta_random}'
            )
            solicit_cred = input('Adquirir credito?: ')
            if solicit_cred.upper() == 'S':
                renda_client = input("Renda mensal: ")
                work_prof = input("Profissão: ")
                if renda_client.isnumeric():
                    renda_client = int(renda_client)
                    if renda_client >= 2000:
                        calculo = (renda_client * 30)
                        limite_disp = (calculo / 100)

                        os.system("clear")
                        print("Credito aprovado!")
                        time.sleep(0.9)
                        os.system("clear")
                        print(
                            f'-=-=-=-=[ Dados bancarios ]-=-=-=-=-\n\n'
                            f'Nome: {nome_client.upper()}\n'
                            f'Agencia: {agencia}\n'
                            f'Conta: {conta_random}\n'
                            f'Limite de credito: R${limite_disp:.2f}'
                        )
                    else:
                        print("Renda incompativel!")
                else:
                    print("Informe apenas numeros.")
            else:
                print("Finalizando sistema...")
        else:
            print("Você precisa ser maior de 18 anos.")
else:
    exit()
