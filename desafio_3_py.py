class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class ContaBancaria:
    def __init__(self, agencia, numero_conta, cliente):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0
        self.limite = 500
        self.numero_saques = 0
        self.extrato = ""

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor, limite_saques):
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > self.limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif self.numero_saques >= limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []
        self.agencia = "0001"

    def criar_cliente(self):
        cpf = input("Informe o CPF (somente número): ")
        if any(cliente.cpf == cpf for cliente in self.clientes):
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        cliente = Cliente(nome, cpf, data_nascimento, endereco)
        self.clientes.append(cliente)
        print("=== Usuário criado com sucesso! ===")

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        cliente = next((c for c in self.clientes if c.cpf == cpf), None)
        if cliente:
            numero_conta = len(self.contas) + 1
            conta = ContaBancaria(self.agencia, numero_conta, cliente)
            self.contas.append(conta)
            cliente.adicionar_conta(conta)
            print("\n=== Conta criada com sucesso! ===")
        else:
            print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

    def listar_contas(self):
        for conta in self.contas:
            linha = f"""\n            Agência:\t{conta.agencia}\n            C/C:\t\t{conta.numero_conta}\n            Titular:\t{conta.cliente.nome}\n"""
            print("=" * 100)
            print(textwrap.dedent(linha))

    def menu(self):
        menu = """\n
        ================ MENU ================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuário
        [q]\tSair
        => """
        return input(textwrap.dedent(menu))

    def executar(self):
        LIMITE_SAQUES = 3
        while True:
            opcao = self.menu()
            if opcao == "d":
                cpf = input("Informe o CPF do titular da conta: ")
                cliente = next((c for c in self.clientes if c.cpf == cpf), None)
                if cliente and cliente.contas:
                    valor = float(input("Informe o valor do depósito: "))
                    cliente.contas[0].depositar(valor)
                else:
                    print("\n@@@ Cliente não encontrado ou sem conta cadastrada! @@@")
            elif opcao == "s":
                cpf = input("Informe o CPF do titular da conta: ")
                cliente = next((c for c in self.clientes if c.cpf == cpf), None)
                if cliente and cliente.contas:
                    valor = float(input("Informe o valor do saque: "))
                    cliente.contas[0].sacar(valor, LIMITE_SAQUES)
                else:
                    print("\n@@@ Cliente não encontrado ou sem conta cadastrada! @@@")
            elif opcao == "e":
                cpf = input("Informe o CPF do titular da conta: ")
                cliente = next((c for c in self.clientes if c.cpf == cpf), None)
                if cliente and cliente.contas:
                    cliente.contas[0].exibir_extrato()
                else:
                    print("\n@@@ Cliente não encontrado ou sem conta cadastrada! @@@")
            elif opcao == "nu":
                self.criar_cliente()
            elif opcao == "nc":
                self.criar_conta()
            elif opcao == "lc":
                self.listar_contas()
            elif opcao == "q":
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    banco = Banco()
    banco.executar()



    




    






