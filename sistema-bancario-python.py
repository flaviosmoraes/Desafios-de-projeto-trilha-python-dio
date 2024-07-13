def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0.00:
        print("\nInsira um valor maior que R$ 0.00")
    elif numero_saques >= limite_saques:
        print(f"\nValor limite de {limite_saques} saques atingido, volte amanhã para conseguir realizar novos saques.")
    elif valor > saldo:
        print("\nSaldo insuficiente.")
    elif valor > limite:
        print(f"\nO valor do saque ultrapassa o limite de R$ {limite:.2f}")
    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: R$ {valor}\n"
        print(f"\nSaque no valor de R${valor:.2f} efetuado com sucesso.\nRetire seu dinheiro na boca do caixa.")
    return saldo, extrato, numero_saques

def deposito(saldo, valor, extrato, /):
    if valor > 0.00:
        saldo += valor
        print(f"\nDeposito no valor de R${valor:.2f} efetuado com sucesso.\nNovo saldo R$ {saldo:.2f} .")
        extrato += f"Depósito: R$ {valor}\n"
    else:
        print("\nInsira um valor maior que R$ 0.00")
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações.\n" if not extrato else extrato)
    print(f"\nSeu saldo é de R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usario(usuarios: list):
    cpf = input("\nDigite o CPF (Somente numeros): ")

    if filtrar_usuario(cpf, usuarios):
        print("Usuário já cadastrado!")
        return

    nome = input("Digite o nome completo: ")
    data_de_nascimento = input("Digite a data de nascimento (dd-mm-aaa): ")
    endereco = input("Digite o endereco (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario = {"cpf": cpf, "nome": nome, "data_de_nascimento": data_de_nascimento, "endereco": endereco}

    usuarios.append(usuario)
    print("Sucesso ao cadastrar usário!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usarios, contas):
    cpf = input("\nDigite o cpf do titular da conta: ")
    usuario = filtrar_usuario(cpf, usarios)
    if usuario:
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("Conta criada com sucesso!")
        return True
    print("Usario não cadastrado!")
    return False

def main():

    MENU = """

[d] Depositar
[s] Sacar
[e] Extrato
[cu] Cadastrar usuário
[cc] Criar conta
[q] Sair

=> """
    LIMITE_SAQUES_DIARIOS = 3
    AGENCIA = "0001"

    saldo = 0.00
    numero_de_saques_diarios = 0
    valor_maximo_por_saque = 500.00
    extrato = ""
    usuarios = []
    contas = []
    contador_contas = 1

    while True:
        opcao = input(MENU)
        
        if opcao == "cu":
            cadastrar_usario(usuarios)
        elif opcao == "cc":
            if criar_conta(AGENCIA, contador_contas, usuarios, contas):
                contador_contas += 1
        elif opcao == "d":
            valor = None
            while not valor:
                try:
                    valor = float(input("\nDigite o valor que deseja depositar R$ "))
                except:
                    print("Insira um valor numérico.")
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "s":
            valor = None
            while not valor:
                try:
                    valor = float(input("\nDigite o valor que deseja sacar R$ "))
                except:
                    print("Insira um valor numérico.")
            saldo, extrato, numero_de_saques_diarios = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=valor_maximo_por_saque,
                numero_saques=numero_de_saques_diarios,
                limite_saques=LIMITE_SAQUES_DIARIOS
                )
        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)
        elif opcao == "q":
            print("\nMuito Obrigado por utilizar nossos serviços!")
            break

main()