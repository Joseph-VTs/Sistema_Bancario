# interface.py

import config as Cores # Importa as cores como 'Cores'
import uteis as Uteis
import verificacoes as Ver
from conta import Cl_Conta # Importa a classe Cl_Conta
from config import Contas_Criadas # Importa a lista global de Contas_Criadas

def Menu_Agencia(Conta_Encontrada):
    while True:
        Uteis.Limpar_Terminal()
        # Usa Cores.Ciano_Ligth e Cores.Reset
        print(f"{Cores.Ciano_Ligth}🏢 Operações na Agência{Cores.Reset}")
        
        # Opções de Menu
        print(f"[{Cores.Ciano_Ligth}1{Cores.Reset}] 💰 - Consultar Saldo")
        print(f"[{Cores.Ciano_Ligth}2{Cores.Reset}] 📄 - Extrato")
        print(f"[{Cores.Ciano_Ligth}3{Cores.Reset}] 💸 - Saque")
        print(f"[{Cores.Ciano_Ligth}4{Cores.Reset}] 💵 - Depósito")
        print(f"[{Cores.Ciano_Ligth}5{Cores.Reset}] 🔁 - Transferência")
        print(f"[{Cores.Ciano_Ligth}6{Cores.Reset}] 📝 - Exportar Extrato para .txt")
        print(f"[{Cores.Ciano_Ligth}0{Cores.Reset}] 🔙 - Voltar")
        
        try:
            # Usa Cores.Black e Cores.Reset
            Ops = int(input(f"{Cores.Black}💢 Escolha uma Opção:{Cores.Reset} "))
        except ValueError:
            # Usa Cores.Red_Ligth e Cores.Reset
            print(f"{Cores.Red_Ligth}❗ Essa não é uma Opção... 😀{Cores.Reset}")
            Uteis.Limpar_Terminal()
            continue

        match Ops:
            case 0: 
                print("Saindo... Voltando ao Menu..."); break
            case 1: 
                print(f"Saldo Atual: R$ {Conta_Encontrada.Get_Saldo()}")
                Uteis.Limpar_Terminal()
            case 2: 
                Conta_Encontrada.Extrato()
            case 3: 
                Conta_Encontrada.Saque_Ag()
            case 4: 
                Conta_Encontrada.Depósito_Ag()
            case 5: 
                Conta_Encontrada.Tranfer()
            case 6: 
                Conta_Encontrada.Exportar_Extrato()
            case _: 
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Não Temos Essa Opção... 🙃{Cores.Reset}")
                Uteis.Limpar_Terminal()

def Menu_Caixa(Conta_Encontrada):
    while True:
        Uteis.Limpar_Terminal()
        # Usa Cores.Ciano_Ligth e Cores.Reset
        print(f"{Cores.Ciano_Ligth}🏧 Operações no Caixa Eletrônico{Cores.Reset}")
        
        # Opções de Menu
        print(f"[{Cores.Ciano_Ligth}1{Cores.Reset}] 💸 - Saque")
        print(f"[{Cores.Ciano_Ligth}2{Cores.Reset}] 💵 - Depósito")
        print(f"[{Cores.Ciano_Ligth}0{Cores.Reset}] 🔙 - Voltar")
        
        try:
            # Usa Cores.Black e Cores.Reset
            Ops = int(input(f"{Cores.Black}💢 Escolha uma Opção:{Cores.Reset} "))
        except ValueError:
            # Usa Cores.Red_Ligth e Cores.Reset
            print(f"{Cores.Red_Ligth}❗ Essa não é uma Opção... 😀{Cores.Reset}")
            Uteis.Limpar_Terminal()
            continue

        match Ops:
            case 0: 
                print("Saindo... Voltando ao Menu..."); break
            case 1: 
                Conta_Encontrada.Saque_Cx()
            case 2: 
                Conta_Encontrada.Depositar_Cx()
            case _: 
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Não Temos Essa Opção... 🙃{Cores.Reset}")
                Uteis.Limpar_Terminal()


def Menu_Cliente(Conta_Encontrada):
    while True:
        Uteis.Limpar_Terminal()
        print("=" * 50)
        # Usa Cores.Ciano e Cores.Reset
        print(f"{Cores.Ciano}🏦 Banco Sentar - Área do Cliente{Cores.Reset}")
        print(f"Titular: {Conta_Encontrada.Get_Titular()} | Conta: {Conta_Encontrada.Get_Numero()}")
        print("-" * 50)
        
        # Opções de Menu
        print(f"[{Cores.Ciano_Ligth}1{Cores.Reset}] 🏢 - Operações na Agência")
        print(f"[{Cores.Ciano_Ligth}2{Cores.Reset}] 🏧 - Operações no Caixa Eletrônico")
        print(f"[{Cores.Ciano_Ligth}3{Cores.Reset}] ⚙️ - Configurações")
        print(f"[{Cores.Ciano_Ligth}4{Cores.Reset}] 📘 - Ver Manual de Uso")
        print(f"[{Cores.Ciano_Ligth}0{Cores.Reset}] 🔙 - Voltar ao Menu Principal")
        print("=" * 50)

        try:
            # Usa Cores.Black e Cores.Reset
            Ops = int(input(f"{Cores.Black}💢 Escolha uma Opção: {Cores.Reset} "))
        except ValueError:
            # Usa Cores.Red_Ligth e Cores.Reset
            print(f"{Cores.Red_Ligth}❗ Essa não é uma Opção... 😀{Cores.Reset}")
            Uteis.Limpar_Terminal()
            continue

        match Ops:
            case 0: 
                print("Saindo... Voltando ao Menu..."); break
            case 1: 
                Menu_Agencia(Conta_Encontrada)
            case 2: 
                Menu_Caixa(Conta_Encontrada)
            case 3: 
                Conta_Encontrada.Config()
            case 4: 
                Uteis.Mostrar_Manual()
            case _: 
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Não Temos Essa Opção... 🙃{Cores.Reset}")
                Uteis.Limpar_Terminal()

def Processar_Login():
    Conta_Selecionada = input("Digite o Número da Conta: ").strip()
    Conta_Encontrada = next((c for c in Contas_Criadas if c.Get_Numero() == Conta_Selecionada), None)

    if not Conta_Encontrada:
        # Usa Cores.Red_Ligth e Cores.Reset
        print(f"{Cores.Red_Ligth}❌ Conta não encontrada. Verifique o número digitado.{Cores.Reset}")
        Uteis.Limpar_Terminal()
        return

    Senha = input("Digite sua Senha: ").strip()

    if Senha != Conta_Encontrada.Get_Senha():
        # Usa Cores.Red_Ligth e Cores.Reset
        print(f"{Cores.Red_Ligth}❌ Senha incorreta. Tente novamente.{Cores.Reset}")
        Uteis.Limpar_Terminal()
        return

    # Usa Cores.Green_Ligth e Cores.Reset
    print(f"{Cores.Green_Ligth}✅ Login realizado com sucesso! Bem-vindo(a), {Conta_Encontrada.Get_Titular()}.{Cores.Reset}")
    Menu_Cliente(Conta_Encontrada)

def Processar_Cadastro():
    # Usa Cores.Ciano_Ligth e Cores.Reset
    print(f"{Cores.Ciano_Ligth}🆕 Cadastro de Novo Cliente{Cores.Reset}")
    Nome1 = Ver.Ver_Str("Digite o Primeiro Nome")
    if Nome1 is None: return
    Nome2 = Ver.Ver_Str("Digite o Segundo Nome")
    if Nome2 is None: return
    Idade = Ver.Ver_Idade()
    if Idade is None: return
    Senha = Ver.Ver_Senha()
    if Senha is None: return

    Nova_Conta = Cl_Conta(Nome1, Nome2, Idade, Senha)
    Contas_Criadas.append(Nova_Conta)

    # Usa Cores.Green_Ligth e Cores.Reset
    print(f"{Cores.Green_Ligth}✅ Conta criada com sucesso!{Cores.Reset}")
    print(f"Titular: {Nova_Conta.Get_Titular()} | Conta: {Nova_Conta.Get_Numero()}")
    # Usa Cores.Yellow_Ligth e Cores.Reset
    input(f"Aperte {Cores.Yellow_Ligth}Enter{Cores.Reset} para Voltar ao Menu.")