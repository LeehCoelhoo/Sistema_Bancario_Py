def menu():
    print("""
            MENU
    ___________________________

    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Criar novo usuário
    [4] Procurar usuário
    [5] Criar nova conta
    [6] Sair
    ___________________________

     """)
    op = input("\nEscolha a opção desejada:")
    return op

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, limite, cont):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = cont >= 3
    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        cont += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, cont

def visu_extrato(saldo, extrato):
    print("""
            EXTRATO
    ___________________________
    """)
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("_______________________________")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = procurar_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def procurar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = procurar_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

def main():
    saldo = 0
    limite = 1000
    extrato = ""
    cont = 0
    usuarios = []
    
    while True:
        opcao = menu()

        if opcao == "0":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "1":
            saldo, extrato, cont = sacar(saldo, extrato, limite, cont)

        elif opcao == "2":
            visu_extrato(saldo, extrato)

        elif opcao == "3":
            criar_usuario(usuarios)

        elif opcao == "4":
            cpf = input("Informe o CPF para procurar o usuário: ")
            usuario = procurar_usuario(cpf, usuarios)
            if usuario:
                print("Usuário encontrado:")
                print(usuario)
            else:
                print("Usuário não encontrado.")

        elif opcao == "5":
            agencia = input("Informe a agência: ")
            numero_conta = input("Informe o número da conta: ")
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                print("Conta criada com sucesso!")
            else:
                print("Conta não criada.")

        elif opcao == "6":
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()



