# 💾 Arquivos Importados
import Cores
import Tabela
import Verifica
import Uteis

#Classe Cliente
class Cla_Cli:
    def __init__(self, Nome: str, SobreNome: str, Idade: int, Senha: str):
        self._Nome = Nome
        self._SobreNome = SobreNome
        self._Idade = Idade
        self._Senha = Senha
        
    # Métodos Getters e Setters
    def Get_Nome(self):
        return self._Nome
    def Set_Nome(self, Novo_Nome):
        Validado = Verifica.Verifica_String(Novo_Nome)
        self._Nome = Validado
        
    def Get_SobreNome(self):
        return self._SobreNome
    def Set_SobreNome(self, Novo_SobreNome):
        Valida = Verifica.Verifica_String(Novo_SobreNome)
        self._SobreNome = Valida
        
    def Get_Idade(self):
        return self._Idade
    def Set_Idade(self, Nova_Idade):
        Valida = Verifica.Verificar_Idade(Nova_Idade)
        self._Idade = Valida
        
    def Get_Senha(self):
        return self._Senha
    def Set_Senha(self, Nova_Senha):
        Valida = Verifica.Verificar_Senha(Nova_Senha)
        self._Senha = Valida
        
    def Titular(self):
        return f"{Cores.Italico}{self.Get_Nome()} {self.Get_SobreNome()}{Cores.Reset}"

#Classe Cartão
class Cla_CT(Cla_Cli):
    def __init__(self, Nome, SobreNome, Idade, Senha):
        super().__init__(Nome, SobreNome, Idade, Senha)
    
        self._Num = Uteis.Random_Conta()
        self._Saldo = 0.0
        self.Historico = []
        
    def Get_Num(self):
        return self._Num
    def Get_Saldo(self):
        return self._Saldo
    
    def Info_User(self):
        return f"\nTitular: {self.Titular} \nIdade: {self.Get_Idade()} \nNúmero da Conta: {self.Get_Num()} \nSaldo: {self.Get_Saldo()} \nSenha: {self.Get_Senha()}"
    
    def __str__(self):
        return self.Info_User()
    
    def Fazer_Pix(self):
        Entrada = input(f"{Cores.White_Ligth}Digite o Valor R$: {Cores.Reset}")
        
        try:
            Valor = float(Entrada)
        except ValueError:
            print(f"{Cores.Red_Ligth}❗ Erro... 🤨 no Entrada{Cores.Reset}")
            return
            
        
        if Valor > 0:
            self._Saldo += Valor
            print(f"{Cores.Green_Ligth}Pix de R$: {Valor:.2f} Realizado com Sucesso para {self.Titular}{Cores.Reset}")
            print(f"{Cores.Yellow_Ligth}Novo Saldo R$: {self.Get_Saldo():.2f}")
        elif Valor < 0:
            print(f"{Cores.Red_Ligth}Valor não pode ser Negativo...{Cores.Reset}")
        else:
            print(f"{Cores.Red_Ligth}❗ Erro... 🤨 no Valor{Cores.Reset}")
            
    def Depositar_Cx(self):
        Entrada = input(f"{Cores.White_Ligth}Digite o Valor R$: ", end="")
        print(",00")
        
        if Entrada > 0:
            self._Saldo += Entrada
            print(f"{Cores.Green_Ligth}✅ Depósito de R$: {Entrada:.0f} Realizado com Sucesso...{Cores.Reset}")
            print(f"{Cores.Yellow_Ligth}Novo Saldo R$: {self.Get_Saldo():.2f}")
        elif Entrada < 0:
            print(f"{Cores.Red_Ligth}❗ Valor não pode ser Negativo... 🙃{Cores.Reset}")
        else:
            print(f"{Cores.Red_Ligth}❗ Erro ao Tentar Depositar... 🙃{Cores.Reset}")
            
            
    def Consultar_Saldo(self):
        print(f"\n--- EXTRATO RÁPIDO ---")
        print(f"Conta: {self.Get_Num()} - Titular: {self.Titular()}")
        print(f"SALDO ATUAL: R$ {self.Get_Saldo():.2f}")
        print("----------------------")
        
    # Extrato Detalhado
    def Detalhe_Ext(self):
        print(f"\n--- EXTRATO DETALHADO ({self.Get_Num()}) ---")
        if not self.Historico:
            print("Nenhuma transação registrada.")
        else:
            for Item in self.Historico:
                print(Item)
        print(f"SALDO FINAL: R$ {self.Get_Saldo():.2f}")
        print("--------------------------------------")
        
c1 = Cla_CT("Joseph", "Ehms", 24, "0123")
Tabela.Contas_Criadas.append(c1)
print(c1.Info_User())
    
def Act_Conta(Conta_Ativa):
    Conta_Ativa.Consultar_Saldo()
    input(f"{Cores.Yellow}Pressione ENTER para voltar ao Menu... {Cores.Reset}")