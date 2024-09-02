
def menu():
    menu = """
    Bem vindo a sua Conta, escolha a opção:

    [d] Depositar
    [s] Sacar
    [e] Extrato    
    [u] Novo Usuário
    [c] Nova Conta
    [q] Sair

    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
     
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if numero_saques >= limite_saques:
        print(f"Você já realizou o limite diário de {limite_saques} saques")           
    elif valor > 0 and valor > saldo:
        print(f"Saque de R$ {valor:.2f} Excedeu o saldo total de R$ {saldo:.2f}")
    elif valor > 0 and valor > limite:
        print(f"Exceu o limite por saque de R$ {limite:.2f}")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")   

    return saldo, extrato, numero_saques    

def mostrar_extrato(saldo, /, *, extrato):
    cabecalho = " Extrato "        
    print("\n" + cabecalho.center(30, "#"))        
    print("\n")
    print("Sem movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n")
    print("".center(30, "#"))

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario_existente = [usuario for usuario in usuarios if usuario["cpf"] == cpf]   

    if usuario_existente:
        print("Já existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!")

def cadastrar_conta(agencia, numero_conta, usuarios, contas):

    cpf = input("Informe o CPF do usuário: ")
    usuario_existente = [usuario for usuario in usuarios if usuario["cpf"] == cpf]   

    if usuario_existente:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": cpf}) 
        print("Conta criada com sucesso!")        
        return 

    print("Usuário não Cadastrado!");    

def main():

    LIMITE_VALOR = 500
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0    
    extrato = ""
    numero_saques = 0    
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)           
            
        elif opcao == "s":

            valor = float(input("Informe o valor do Saque: "))

            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=LIMITE_VALOR, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)

        elif opcao == "e":

            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            
            cadastrar_usuario(usuarios)    

        elif opcao == "c":

            numero_conta = len(contas) + 1
            cadastrar_conta(AGENCIA, numero_conta, usuarios, contas)
                   

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()