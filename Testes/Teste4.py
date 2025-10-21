import random
from dataclasses import dataclass, field

# Lista global de contas criadas
Contas_Criadas = []

def Random_Conta():
    return f"{random.randint(0, 999999):06d}"

# ------------------------------
# CLASSES
# ------------------------------

@dataclass
class Cliente:
    nome1: str
    nome2: str
    idade: str
    senha: str

    @property
    def titular(self):
        return f"{self.nome1} {self.nome2}"

@dataclass
class Conta(Cliente):
    numero: str = field(default_factory=Random_Conta)
    saldo: float = 0.0
    historico: list = field(default_factory=list)

    def info(self):
        return f"\nTitular: {self.titular} \nConta: {self.numero} \nSaldo R$: {self.saldo:.2f}"

    def __str__(self):
        return self.info()

    def fazer_pix(self):
        try:
            valor = float(input("Digite o Valor: R$ "))
        except ValueError:
            print("Valor inválido.")
            return

        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Pix recebido: R$ {valor:.2f}")
            print(f"\n✅ Pix de R$ {valor:.2f} realizado com sucesso para {self.titular}")
            print(f"Novo Saldo: R$ {self.saldo:.2f}")
        else:
            print("❌ Valor deve ser positivo.")

    def consultar_saldo(self):
        print(f"\n--- EXTRATO RÁPIDO ---")
        print(f"Conta: {self.numero} - Titular: {self.titular}")
        print(f"SALDO ATUAL: R$ {self.saldo:.2f}")
        print("----------------------")

    def ver_extratos(self):
        print(f"\n--- EXTRATO DETALHADO ({self.numero}) ---")
        if not self.historico:
            print("Nenhuma transação registrada.")
        else:
            for item in self.historico:
                print(item)
        print(f"SALDO FINAL: R$ {self.saldo:.2f}")
        print("--------------------------------------")

    def depositar(self):
        try:
            valor = float(input("Valor do depósito: R$ "))
        except ValueError:
            print("Valor inválido.")
            return

        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: R$ {valor:.2f}")
            print(f"✅ Depósito realizado com sucesso. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("❌ Valor deve ser positivo.")

    def sacar(self):
        try:
            valor = float(input("Valor do saque: R$ "))
        except ValueError:
            print("Valor inválido.")
            return

        if valor <= 0:
            print("❌ Valor deve ser positivo.")
        elif valor > self.saldo:
            print("❌ Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.historico.append(f"Saque: R$ {valor:.2f}")
            print(f"✅ Saque realizado com sucesso. Novo saldo: R$ {self.saldo:.2f}")

    def transferir(self):
        destino = input("Número da conta de destino: ")
        conta_destino = next((c for c in Contas_Criadas if c.numero == destino), None)

        if not conta_destino:
            print("❌ Conta de destino não encontrada.")
            return

        try:
            valor = float(input("Valor da transferência: R$ "))
        except ValueError:
            print("Valor inválido.")
            return

        if valor <= 0:
            print("❌ Valor deve ser positivo.")
        elif valor > self.saldo:
            print("❌ Saldo insuficiente.")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico.append(f"Transferência enviada para {conta_destino.titular}: R$ {valor:.2f}")
            conta_destino.historico.append(f"Transferência recebida de {self.titular}: R$ {valor:.2f}")
            print(f"✅ Transferência realizada com sucesso para {conta_destino.titular}.")
            print(f"Novo saldo: R$ {self.saldo:.2f}")
            
    def exportar_extrato(self):
        nome_arquivo = f"extrato_{self.numero}.txt"
        try:
            with open(nome_arquivo, "w", encoding="utf-8") as f:
                f.write(f"Extrato da Conta: {self.numero}\n")
                f.write(f"Titular: {self.titular}\n")
                f.write(f"Idade: {self.idade}\n")
                f.write(f"Saldo Atual: R$ {self.saldo:.2f}\n")
                f.write("\n--- Histórico de Transações ---\n")
                if not self.historico:
                    f.write("Nenhuma transação registrada.\n")
                else:
                    for item in self.historico:
                        f.write(f"{item}\n")
                f.write("-------------------------------\n")
            print(f"✅ Extrato exportado com sucesso para o arquivo: {nome_arquivo}")
        except Exception as e:
            print(f"❌ Erro ao exportar extrato: {e}")

# ------------------------------
# FUNÇÕES DO SISTEMA
# ------------------------------

def lista_clientes():
    if not Contas_Criadas:
        print("\nNenhuma Conta Cadastrada.")
        return

    print("\n--- Contas Cadastradas ---")
    for i, conta in enumerate(Contas_Criadas):
        print(f"[{i + 1}] {conta}")
    print("--------------------------")

def pix():
    lista_clientes()
    while True:
        chave = input("Digite o Número da Conta (Chave) ou 0 para Sair: ")
        if chave == '0':
            print("Saindo...")
            return

        conta_destino = next((c for c in Contas_Criadas if c.numero == chave), None)
        if conta_destino:
            conta_destino.fazer_pix()
            return
        else:
            print("\n❌ Nenhuma Conta Cadastrada com esse número.")

def menu(conta_ativa):
    while True:
        print(f"\n--- Menu de Transações - {conta_ativa.nome1} ---")
        print("1 - Ver Contas")
        print("2 - Fazer Pix")
        print("3 - Info")
        print("4 - Ver Extrato")
        print("5 - Depositar")
        print("6 - Sacar")
        print("7 - Transferir")
        print("8 - Exportar Extrato")
        print("0 - Sair")

        opcao = input("Digite uma Opção: ")

        if opcao == '0':
            print("Saindo...")
            break
        elif opcao == '1':
            lista_clientes()
        elif opcao == '2':
            pix()
        elif opcao == '3':
            conta_ativa.consultar_saldo()
        elif opcao == '4':
            conta_ativa.ver_extratos()
        elif opcao == '5':
            conta_ativa.depositar()
        elif opcao == '6':
            conta_ativa.sacar()
        elif opcao == '7':
            conta_ativa.transferir()
        elif opcao == '8':
            conta_ativa.exportar_extrato()
        else:
            print("Opção Inválida...")

def cadastro():
    print("\n--- Cadastro de Nova Conta ---")
    nome1 = input("Nome 1: ")
    nome2 = input("Nome 2: ")
    idade = input("Idade: ")
    senha = input("Senha: ")

    nova_conta = Conta(nome1, nome2, idade, senha)
    Contas_Criadas.append(nova_conta)

    print("✅ Cadastrado com Sucesso...")
    print(f"Número da Conta Gerado: {nova_conta.numero}")
    print(f"Detalhes: \n{nova_conta.info()}")
    input("Pressione ENTER para voltar ao Menu...")

def entrada():
    num = input("Número da Conta: ")
    senha = input("Senha: ")

    conta_logada = next((c for c in Contas_Criadas if c.numero == num and c.senha == senha), None)

    if conta_logada:
        print(f"\n✅ Login bem-sucedido. Bem-vindo(a), {conta_logada.titular}!")
        menu(conta_logada)
    else:
        print("❌ Conta ou senha incorreta.")

def comeco():
    while True:
        print("\nA - Entrar")
        print("B - Cadastrar")
        print("0 - Sair")

        ops = input("Digite uma Opção: ").upper()

        if ops == '0':
            print("Saindo...")
            break
        elif ops == 'A':
            entrada()
        elif ops == 'B':
            cadastro()
        else:
            print("Não é uma Opção...")

# ------------------------------
# INICIAR SISTEMA
# ------------------------------

comeco()