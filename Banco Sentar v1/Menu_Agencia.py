# 💾 Arquivos Importados
import Cores
import Uteis
import Menu_Caixa
import Classe



def Agencia():
    while True:
        Uteis.Limpar_Terminal()

        print("=" * 50)
        print(f"Seja Bem-Vindo ao {Cores.Blue}Banco Sentar.{Cores.Reset}")
        print("-" * 50)
        print(f"{Cores.Fundo_Magenta}{'Agência Bancária'.center(20)}{Cores.Reset}")
        print(f"[{Cores.Ciano_Ligth}1{Cores.Reset}] ⚙️ - Configurações")
        print(f"[{Cores.Ciano_Ligth}2{Cores.Reset}] 📈 - Gerar Cartão")
        print(f"[{Cores.Ciano_Ligth}3{Cores.Reset}] 📈 - Gerar Chave Pix")
        print()
        print(f"{Cores.Fundo_Magenta}{'Extratos Separados'.center(20)}{Cores.Reset}")
        print(f"[{Cores.Ciano_Ligth}4{Cores.Reset}] 📄 - Crédito")
        print(f"[{Cores.Ciano_Ligth}5{Cores.Reset}] 📄 - Débito")
        print()
        print(f"{Cores.Fundo_Magenta}{'Outras Opções'.center(20)}{Cores.Reset}")
        print(f"[{Cores.Ciano_Ligth}6{Cores.Reset}] 🏧 - Caixa Eletrônico")
        print(f"[{Cores.Ciano_Ligth}0{Cores.Reset}] ↩ - Voltar...")
        print("=" * 50)
        
        try:
            Options_Menu = int(input(f"{Cores.Black}💢 Escolha uma Opção:{Cores.Reset} "))
        except ValueError:
            print(f"{Cores.Red_Ligth}❗ Essa não é uma Opção... 😀{Cores.Reset}")
            continue
        
        match Options_Menu:
            case 1: print("Opção")
            case 2: print("Opção")
            case 3: print("Opção")
            case 4: print("Opção")
            case 5: print("🏧 Entrando no Caixa Eletrônico... "); Menu_Caixa.Caixa()
            case 0: print("Voltando..."); break
            case _: print("Não é Opção")