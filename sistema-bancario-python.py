menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.00
numero_de_saques_diarios = 0
LIMITE_SAQUES_DIARIOS = 3
valor_maximo_por_saque = 500.00
historico_operacoes = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = None
        while not valor:
            try:
                valor = float(input("\nDigite o valor que deseja depositar R$ "))
                if valor > 0.00:
                    saldo += valor
                    historico_operacoes.append(valor)
                    print(f"\nDeposito no valor de R${valor:.2f} efetuado com sucesso.\nNovo saldo R$ {saldo:.2f} .")
                else:
                    print("\nInsira um valor maior que R$ 0.00")
            except:
                print("\nDigite um valor numérico!")

    elif opcao == "s":
        valor = None
        while not valor:
            try:
                valor = float(input("\nDigite o valor que deseja sacar R$ "))
                if valor > 0.00:
                    if numero_de_saques_diarios < LIMITE_SAQUES_DIARIOS:
                        if saldo >= valor:
                            if valor <= valor_maximo_por_saque:
                                saldo -= valor
                                numero_de_saques_diarios += 1
                                historico_operacoes.append(-valor)
                                print(f"\nSaque no valor de R${valor:.2f} efetuado com sucesso.\nRetire seu dinheiro na boca do caixa.")
                            else:
                                print("\nO valor do saque ultrapassa o limite de R$ 500.00")
                        else:
                            print("\nSaldo insuficiente.")
                    else:
                        print(f"\nValor limite de {LIMITE_SAQUES_DIARIOS} saques atingido, volte amanhã para conseguir realizar novos saques.")
                else:
                    print("\nInsira um valor maior que R$ 0.00")
            except:
                print("\nDigite um valor numérico!")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if historico_operacoes:
            for operacao in historico_operacoes:
                if operacao > 0.00:
                    print(f"Depósito: R$ {operacao:.2f}")
                else:
                    print(f"Saque: R$ {-operacao:.2f}")
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSeu saldo é de R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("\nMuito Obrigado por utilizar nossos serviços!")
        break