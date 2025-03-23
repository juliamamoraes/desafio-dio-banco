class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        """Realiza o depósito na conta."""
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        """Realiza o saque da conta."""
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def exibir_extrato(self):
        """Exibe o extrato da conta."""
        if not self.extrato:
            print("Extrato vazio.")
        else:
            print("Extrato da conta:")
            for transacao in self.extrato:
                print(transacao)
            print(f"Saldo atual: R${self.saldo:.2f}")

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Menu ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Exibir Extrato")
    print("4. Sair")
    
def main():
    """Função principal que controla o sistema bancário."""
    print("Bem-vindo ao Sistema Bancário!")
    nome = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(nome)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: R$"))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: R$"))
            conta.sacar(valor)
        elif opcao == "3":
            conta.exibir_extrato()
        elif opcao == "4":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()






