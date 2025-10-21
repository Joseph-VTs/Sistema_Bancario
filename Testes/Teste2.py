# usar @property para simplificar os getters, ou até usar dataclasses para reduzir a verbosidade.


import random

Contas_Criadas = []

def Random_Conta():
    return f"{random.randint(0, 999999):06d}"

class Cla_Cli:
    def __init__(self, Nome1, Nome2, Idade, Senha):
        self._Nome1 = Nome1
        self._Nome2 = Nome2
        self._Idade = Idade
        self._Senha = Senha
        
    def Get_Nome1(self): return self._Nome1
    def Set_Nome1(self, New): self._Nome1 = New
        
    def Get_Nome2(self): return self._Nome2
    def Set_Nome2(self, New): self._Nome2 = New
        
    def Get_Idade(self): return self._Idade
    def Set_Idade(self, New): self._Idade = New
        
    def Get_Senha(self): return self._Senha
    def Set_Senha(self, New): self._Senha = New
        
    def Titular(self): return f"{self._Nome1} {self._Nome2}"

class Cla_CT(Cla_Cli):
    def __init__(self, Nome1, Nome2, Idade, Senha):
        super().__init__(Nome1, Nome2, Idade, Senha)
        self._Num = Random_Conta()
        self._Saldo = 0.0
        self.Historico = []
        
    def Get_Num(self): return self._Num
    def Get_Saldo(self): return self._Saldo
        
    def Info(self):
        return f"\nTitular: {self.Titular()} \nConta: {self._Num} \nSaldo R$: {self._Saldo:.2f}"
        
    def __str__(self): return self.Info()
        
    def Fazer_Pix(self):
        try:
            Valor = float(input("Digite o Valor: R$ "))
        except ValueError:
            print("Valor inválido.")
            return

        if Valor > 0:
            self._Saldo += Valor
            self.Historico.append(f"Pix recebido: R$ {Valor:.2f}")
            print(f"\n✅ Pix de R$ {Valor:.2f} realizado com sucesso para {self.Titular()}")
            print(f"Novo Saldo: R$ {self._Saldo:.2f}")
        else:
            print("❌ Valor deve ser positivo.")
            
    def Consultar_Saldo(self):
        print(f"\n--- EXTRATO RÁPIDO ---")
        print(f"Conta: {self._Num} - Titular: {self.Titular()}")
        print(f"SALDO ATUAL: R$ {self._Saldo:.2f}")
        print("----------------------")
        
    def Ver_Extratos(self):
        print(f"\n--- EXTRATO DETALHADO ({self._Num}) ---")
        if not self.Historico:
            print("Nenhuma transação registrada.")
        else:
            for Item in self.Historico:
                print(Item)
        print(f"SALDO FINAL: R$ {self._Saldo:.2f}")
        print("--------------------------------------")

def Lista_Clientes():
    if not Contas_Criadas:
        print("\nNenhuma Conta Cadastrada.")
        return
    
    print("\n--- Contas Cadastradas ---")
    for i, conta in enumerate(Contas_Criadas):
        print(f"[{i + 1}] {conta}") 
    print("--------------------------")
        
def Pix():
    Lista_Clientes()
    while True:
        Chave_Num = input("Digite o Número da Conta (Chave) ou 0 para Sair: ")
        if Chave_Num == '0':
            print("Saindo...")
            return
        
        Conta_Destino = next((c for c in Contas_Criadas if c.Get_Num() == Chave_Num), None)
        if Conta_Destino:
            Conta_Destino.Fazer_Pix()
            return
        else:
            print("\n❌ Nenhuma Conta Cadastrada com esse número.")

def Menu(Conta_Ativa):
    while True:
        print(f"\n--- Menu de Transações - {Conta_Ativa.Get_Nome1()} ---")
        print("1 - Ver Contas")
        print("2 - Fazer Pix")
        print("3 - Info")
        print("4 - Ver Extrato")
        print("0 - Sair")
        
        Ops = input("Digite uma Opção: ")
        
        if Ops == '0':
            print("Saindo...")
            break
        elif Ops == '1':
            Lista_Clientes()
        elif Ops == '2':
            Pix()
        elif Ops == '3':
            Conta_Ativa.Consultar_Saldo()
        elif Ops == '4':
            Conta_Ativa.Ver_Extratos()
        else:
            print("Opção Inválida...")

def Cadastro():
    print("\n--- Cadastro de Nova Conta ---")
    Nome1 = input("Nome 1: ")
    Nome2 = input("Nome 2: ")
    Idade = input("Idade: ")
    Senha = input("Senha: ")
    
    New_CL = Cla_CT(Nome1, Nome2, Idade, Senha)
    Contas_Criadas.append(New_CL)
    
    print("✅ Cadastrado com Sucesso...")
    print(f"Número da Conta Gerado: {New_CL.Get_Num()}")
    print(f"Detalhes: \n{New_CL.Info()}")
    input("Pressione ENTER para voltar ao Menu...")

def Entrada():
    Num_Conta = input("Número da Conta: ")
    Senha = input("Senha: ")
    
    Conta_Log = next((c for c in Contas_Criadas if c.Get_Num() == Num_Conta), None)
    
    if Conta_Log and Conta_Log.Get_Senha() == Senha:
        print(f"\n✅ Login bem-sucedido. Bem-vindo(a), {Conta_Log.Titular()}!")
        Menu(Conta_Log)
    else:
        print("❌ Conta ou senha incorreta.")

def Comeco():
    while True:
        print("\nA - Entrar")
        print("B - Cadastrar")
        print("0 - Sair")
        
        Ops = input("Digite uma Opção: ").upper()
        
        if Ops == '0':
            print("Saindo...")
            break
        elif Ops == 'A':
            Entrada()
        elif Ops == 'B':
            Cadastro()
        else:
            print("Não é uma Opção...")

Comeco()