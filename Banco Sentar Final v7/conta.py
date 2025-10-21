# conta.py

import config as Cores # Importa as cores como 'Cores'
import uteis as Uteis
import verificacoes as Ver
from cliente import Cl_Cliente # Importa a classe base
from config import Contas_Criadas # Importa a lista global de Contas_Criadas
from config import Notas_Aceitas

# Classe da Conta (Herda de Cliente)
class Cl_Conta(Cl_Cliente):
    def __init__(self, Nome1, Nome2, Idade, Senha):
        super().__init__(Nome1,Nome2, Idade)
        
        self._Numero = Uteis.Random_Conta()
        self._Senha = Senha
        self._Saldo = 0.0
        self._Historico = []
        
    def Get_Numero(self): return self._Numero
    def Set_Numero(self, New): 
        # Esta função Set_Numero não foi definida com validação no original,
        # mas no Config() do original existe a opção, então a deixamos simples.
        self._Numero = New
    
    def Get_Senha(self): return self._Senha
    def Set_Senha(self):
        New = Ver.Ver_Senha()
        if New:
            self._Senha = New
    
    def Get_Saldo(self): return f"{self._Saldo:.2f}"
    
    def Get_Historico(self): return self._Historico
    
    def Config(self):
        
        while True:
            Uteis.Limpar_Terminal()
            print(
                f"Informações da Conta. {Cores.Ciano_Ligth}🏦 Banco Sentar{Cores.Reset}.",
                f"\n{Cores.Blue_Ligth}Primeiro Nome: {self.Get_Nome1()}{Cores.Reset}",
                f"\n{Cores.Blue_Ligth}Segundo Nome: {self.Get_Nome2()}{Cores.Reset}",
                f"\n{Cores.Blue_Ligth}Idade: {self.Get_Idade()}{Cores.Reset}",
                f"\n{Cores.Blue_Ligth}N° da Conta: {self.Get_Numero()}{Cores.Reset}",
                f"\n{Cores.Blue_Ligth}Saldo R$: {self.Get_Saldo()}{Cores.Reset}",
                f"\n{Cores.Blue_Ligth}Senha: {self.Get_Senha()}{Cores.Reset} \n"
            )
            
            # Opções de Menu
            print(f"[{Cores.Ciano_Ligth}1{Cores.Reset}] - Alterar Primeiro Nome")
            print(f"[{Cores.Ciano_Ligth}2{Cores.Reset}] - Alterar Segundo Nome")
            print(f"[{Cores.Ciano_Ligth}3{Cores.Reset}] - Alterar Idade")
            print(f"[{Cores.Ciano_Ligth}4{Cores.Reset}] - Alterar N° da Conta")
            print(f"[{Cores.Ciano_Ligth}5{Cores.Reset}] - Alterar Senha")
            print(f"[{Cores.Ciano_Ligth}0{Cores.Reset}] - Voltar...")
            
            try:
                Ops = int(input("Digite uma Opção: ").strip())
            except ValueError:
                print(f"{Cores.Yellow}❗ Entrada Inválida. Por Favor Tente Novamente.{Cores.Reset}")
                continue
            
            match Ops:
                case 0: 
                    print("Saindo... Volte Sempre que quiser Descançar..."); break
                case 1:
                    self.Set_Nome1()
                case 2:
                    self.Set_Nome2()
                case 3:
                    self.Set_Idade()
                case 4:
                    self.Set_Numero() # No original a função não tem parâmetro para Set_Numero,
                                      # mas o Ver_Str ou uma validação similar seria mais adequado aqui.
                                      # Mantendo o fluxo original, não há entrada de dado.
                    pass # Adicionar lógica de entrada e validação se necessário.
                case 5:
                    self.Set_Senha()
                case _:
                    print(f"{Cores.Yellow_Ligth}❗ Não Temos Essa Opção... 🙃{Cores.Reset}")
        
    def __str__(self):
        return (
            f"Informações da Conta. {Cores.Ciano_Ligth}🏦 Banco Sentar{Cores.Reset}.\n"
            f"{Cores.Blue_Ligth}Primeiro Nome: {self.Get_Nome1()}{Cores.Reset}\n"
            f"{Cores.Blue_Ligth}Segundo Nome: {self.Get_Nome2()}{Cores.Reset}\n"
            f"{Cores.Blue_Ligth}Idade: {self.Get_Idade()}{Cores.Reset}\n"
            f"{Cores.Blue_Ligth}N° da Conta: {self.Get_Numero()}{Cores.Reset}\n"
            f"{Cores.Blue_Ligth}Saldo R$: {self.Get_Saldo()}{Cores.Reset}\n"
        )

    
    def Fazer_Pix(self):
        while True:
            Destino = input("Digite o Número da Conta de Destino: ").strip()
            if Destino.lower() == "sair":
                print(f"{Cores.Yellow_Ligth}❗ Operação cancelada pelo usuário.{Cores.Reset}")
                return None
            Conta_Destino = next((c for c in Contas_Criadas if c.Get_Numero() == Destino), None)

            if Conta_Destino == self:
                print(f"{Cores.Yellow_Ligth}❗ Não é possível enviar Pix para a própria conta.{Cores.Reset}")
                continue

            if not Conta_Destino:
                print(f"{Cores.Red_Ligth}❌ Conta de destino não encontrada.{Cores.Reset}")
                return

            Valor = input("Digite o Valor R$: ").strip().replace(",", ".")

            if Valor.lower() == "sair":
                print(f"{Cores.Yellow_Ligth}❗ Operação cancelada pelo usuário.{Cores.Reset}")
                return None

            try:
                Value_Convert = float(Valor)
            except ValueError:
                print(f"{Cores.Yellow}❗ Entrada Inválida. Por Favor Tente Novamente.{Cores.Reset}")
                continue

            if Value_Convert <= 0:
                print(f"{Cores.Yellow_Ligth}❗ Valor deve ser Maior que Zero.{Cores.Reset}")
                continue

            if Value_Convert > self._Saldo:
                print(f"{Cores.Red_Ligth}❗ Saldo Insuficiente para Realizar essa Transação.{Cores.Reset}")
                continue

            # Realiza o Pix
            self._Saldo -= Value_Convert
            Conta_Destino._Saldo += Value_Convert

            # Registra no histórico
            self._Historico.append(f"⚡ [{Uteis.Agora_hr()}] Pix enviado para {Conta_Destino.Get_Titular()} | R$ {Value_Convert:.2f}")
            Conta_Destino._Historico.append(f"⚡ [{Uteis.Agora_hr()}] Pix recebido de {self.Get_Titular()} | R$ {Value_Convert:.2f}")

            print(f"{Cores.Green_Ligth}✅ Pix de R$ {Value_Convert:.2f} enviado com sucesso para {Conta_Destino.Get_Titular()}.{Cores.Reset}")
            print(f"Novo saldo: R$ {self.Get_Saldo()}")
            input("Aperte Enter para sair: ")
            break

        
    # Extrato Detalhado
    def Extrato(self):
        print(f"\n{Cores.Ciano_Ligth}----- Extrato Detalhado. Conta: {self._Numero} -----{Cores.Reset}")
        print(f"Titular: {self.Get_Titular()} | Consulta em: {Uteis.Agora_hr()}")
        print("-" * 55)

        if not self._Historico:
            print(f"{Cores.Yellow_Ligth}Nenhuma Transação Registrada.{Cores.Reset}")
        else:
            for i, item in enumerate(self._Historico, start=1):
                print(f"[{i}] ➤ {item}")

        print("-" * 55)
        print(f"{Cores.Green_Ligth}Saldo Atual R$: {self.Get_Saldo()}{Cores.Reset}")
        print(f"{Cores.Ciano_Ligth}-------------------------------------------------------{Cores.Reset}")
        input("Aperte Enter para sair: ")
        
    # Exportar Arquivo .txt
    def Exportar_Extrato(self):
        Nome_Arquivo = f"Extrato_{self.Get_Numero()}.txt"
        try:
            with open(Nome_Arquivo, "w", encoding="utf-8") as arquivo:
                arquivo.write(f"🏦 Banco Sentar - Extrato Detalhado\n")
                arquivo.write(f"Titular: {self.Get_Titular()}\n")
                arquivo.write(f"Número da Conta: {self.Get_Numero()}\n")
                arquivo.write(f"Data da Consulta: {Uteis.Agora_hr()}\n")
                arquivo.write("-" * 50 + "\n")

                if not self._Historico:
                    arquivo.write("Nenhuma Transação Registrada.\n")
                else:
                    for i, item in enumerate(self._Historico, start=1):
                        arquivo.write(f"[{i}] ➤ {item}\n")

                arquivo.write("-" * 50 + "\n")
                arquivo.write(f"Saldo Atual: R$ {self.Get_Saldo()}\n")
                arquivo.write("=" * 50 + "\n")

            print(f"{Cores.Green_Ligth}✅ Extrato exportado com sucesso para o arquivo: {Nome_Arquivo}{Cores.Reset}")
        except Exception as e:
            print(f"{Cores.Red_Ligth}❌ Erro ao exportar o extrato: {e}{Cores.Reset}")

        
    #Depósito feito no Caixa Eletrônico
    def Depositar_Cx(self):
        while True:
            # Usa Cores.Yellow e Cores.Reset
            print(f"{Cores.Yellow}Apenas Notas de (R$20, R$50 ou R$100) são Aceitas nesse Terminal.{Cores.Reset}")        
            Entrada = input("Digite o Valor para Depósito (ou digite 'sair' para cancelar): ").strip()

            if Entrada.lower() == "sair":
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Depósito cancelado pelo usuário.{Cores.Reset}")
                break

            if not Entrada.isdigit():
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Valor deve ser um Número Inteiro.{Cores.Reset}")
                continue

            Value_Convert = int(Entrada)

            if not Ver.Valor_Validado(Value_Convert, Notas_Aceitas):
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Valor Inválido. Só são permitidos Depósitos de R$20, R$50 ou R$100.{Cores.Reset}")
                continue

            self._Saldo += Value_Convert
            self._Historico.append(f"💵 Depósito no Caixa Eletrônico: R$ {Value_Convert:.2f}")
            # Usa Cores.Green_Ligth e Cores.Reset
            print(f"{Cores.Green_Ligth}✅ Depósito de R$ {Value_Convert:.2f} realizado com sucesso!{Cores.Reset}")
            print(f"Novo saldo: R$ {self.Get_Saldo()}")
            input("Aperte Enter Para sair: ")
            break

            
    #Saque feito no Caixa Eletrônico
    def Saque_Cx(self):
        while True:
            Entrada = input("Digite o Valor para Sacar R$ (ou digite 'sair' para cancelar): ").strip()

            if Entrada.lower() == "sair":
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Saque cancelado pelo usuário.{Cores.Reset}")
                break

            if not Entrada.isdigit():
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Valor deve ser um Número Inteiro.{Cores.Reset}")
                continue

            Value_Convert = int(Entrada)

            if not Ver.Valor_Validado(Value_Convert, Notas_Aceitas):
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Valor Inválido. Só são permitidos Saques de R$20, R$50 ou R$100.{Cores.Reset}")
                continue

            if Value_Convert > self._Saldo:
                # Usa Cores.Red_Ligth e Cores.Reset
                print(f"{Cores.Red_Ligth}❗ Saldo insuficiente para saque.{Cores.Reset}")
                continue

            self._Saldo -= Value_Convert
            self._Historico.append(f"💸 Saque no Caixa Eletrônico: R$ {Value_Convert:.2f}")
            # Usa Cores.Green_Ligth e Cores.Reset
            print(f"{Cores.Green_Ligth}✅ Saque de R$ {Value_Convert:.2f} realizado com sucesso!{Cores.Reset}")
            print(f"Novo saldo: R$ {self.Get_Saldo()}")
            input("Aperte Enter Para sair: ")
            break

        
        
    # Depósito na Agência
    def Depósito_Ag(self):
        Valor_Ent = Ver.Ver_Float()

        # O valor pode ser None se o usuário digitou 'sair'
        if Valor_Ent is None:
            return

        self._Saldo += Valor_Ent
        self._Historico.append(f"🏢 [{Uteis.Agora_hr()}] Depósito via Agência: R$ {Valor_Ent:.2f}")

        # Usa Cores.Green_Ligth e Cores.Reset
        print(f"{Cores.Green_Ligth}✅ Depósito de R$ {Valor_Ent:.2f} Realizado com sucesso!{Cores.Reset}")
        print(f"Novo saldo: R$ {self.Get_Saldo()}")
        input("Aperte Enter para sair: ")

        
    # Saque na Agência
    def Saque_Ag(self):
        Valor_Ent = Ver.Ver_Float()

        # O valor pode ser None se o usuário digitou 'sair'
        if Valor_Ent is None:
            return

        if Valor_Ent > self._Saldo:
            # Usa Cores.Red_Ligth e Cores.Reset
            print(f"{Cores.Red_Ligth}❗ Saldo insuficiente para saque.{Cores.Reset}")
            return

        self._Saldo -= Valor_Ent
        self._Historico.append(f"🏢 [{Uteis.Agora_hr()}] Saque via Agência: R$ {Valor_Ent:.2f}")

        # Usa Cores.Green_Ligth e Cores.Reset
        print(f"{Cores.Green_Ligth}✅ Saque de R$ {Valor_Ent:.2f} Realizado com sucesso!{Cores.Reset}")
        print(f"Novo saldo: R$ {self.Get_Saldo()}")
        input("Aperte Enter para sair: ")

        
    def Tranfer(self):
        while True:
            try:
                Destino = input("Conta Destino: ").strip()
            except ValueError:
                # Usa Cores.Yellow e Cores.Reset
                print(f"{Cores.Yellow}❗ Entrada Inválida. Por Favor Tente Novamente.{Cores.Reset}")
                continue
            
            if Destino.lower() == "sair":
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Operação cancelada pelo usuário.{Cores.Reset}")
                return None

            Conta_Destino = next((c for c in Contas_Criadas if c.Get_Numero() == Destino), None)

            if Conta_Destino == self:
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Não é possível Transferir para a Própria Conta.{Cores.Reset}")
                continue

            if not Conta_Destino:
                # Usa Cores.Red_Ligth e Cores.Reset
                print(f"{Cores.Red_Ligth}❌ Conta de destino não encontrada.{Cores.Reset}")
                return

            Entrada = input("Digite o Valor da Transferência R$: ").strip().replace(",", ".")

            if Entrada.lower() == "sair":
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Operação cancelada pelo usuário.{Cores.Reset}")
                return None

            try:
                Value_Convert = float(Entrada)
            except ValueError:
                # Usa Cores.Yellow e Cores.Reset
                print(f"{Cores.Yellow}❗ Entrada Inválida. Por Favor Tente Novamente.{Cores.Reset}")
                continue
            
            if Value_Convert <= 0:
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ O Valor deve ser Maior que Zero.{Cores.Reset}")
                continue

            Saldo = float(self.Get_Saldo().replace(",", "."))

            if Value_Convert > Saldo:
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Saldo Insuficiente para essa Transferência.{Cores.Reset}")
                continue

            # Realizando a Transferência
            self._Saldo -= Value_Convert
            Conta_Destino._Saldo += Value_Convert

            # Atualizando o Histórico/Extrato
            self._Historico.append(
                f"🔁 [{Uteis.Agora_hr()}] Transferência Enviada para {Conta_Destino.Get_Titular()} | R$ {Value_Convert:.2f}"
            )
            Conta_Destino._Historico.append(
                f"🔁 [{Uteis.Agora_hr()}] Transferência Recebida de {self.Get_Titular()} | R$ {Value_Convert:.2f}"
            )

            # Comprovante
            print("-" * 50)
            # Usa Cores.Ciano_Ligth e Cores.Reset
            print(f"{Cores.Ciano_Ligth}📄 Comprovante de Transferência{Cores.Reset}")
            print(f"Data/Hora: {Uteis.Agora_hr()}")
            print(f"De: {self.Get_Titular()} | Conta: {self.Get_Numero()}")
            print(f"Para: {Conta_Destino.Get_Titular()} | Conta: {Conta_Destino.Get_Numero()}")
            print(f"Valor Transferido: R$ {Value_Convert:.2f}")
            print("-" * 50)

            # Usa Cores.Green_Ligth e Cores.Reset
            print(f"{Cores.Green_Ligth}✅ Transferência Realizada com sucesso!{Cores.Reset}")
            print(f"Novo saldo: R$ {self._Saldo:.2f}")
            # Usa Cores.Yellow_Ligth e Cores.Reset
            input(f"Aperte {Cores.Yellow_Ligth}Enter{Cores.Reset} para Voltar ao Menu.")
            break