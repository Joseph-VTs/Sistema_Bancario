# 💾 Arquivos Importados
import Cores
import Uteis


def Caixa():
    while True:
        Uteis.Limpar_Terminal()
        
        print("=" * 50)
        print(f"🏧 Caixa Eletrônico. {Cores.Blue}Banco Sentar{Cores.Reset}")
        print("-" * 50)
        print(f"[{Cores.Ciano_Ligth}1{Cores.Reset}] - 📄 Extrato")
        print(f"[{Cores.Ciano_Ligth}2{Cores.Reset}] - 📤 Sacar")
        print(f"[{Cores.Ciano_Ligth}3{Cores.Reset}] - 📥 Depositar")
        print(f"[{Cores.Ciano_Ligth}4{Cores.Reset}] - 🔁 Tranferência")
        print(f"[{Cores.Ciano_Ligth}0{Cores.Reset}] - ↩ Voltar à Agência...")
        print("=" * 50)
        
        try:
            Options_Menu = int(input(f"{Cores.Black}💢 Escolha uma Opção:{Cores.Reset} "))
        except ValueError:
            print(f"{Cores.Red_Ligth}❗ Essa não é uma Opção... 😀{Cores.Reset}")
            continue
        
        match Options_Menu:
            case 1:
                print("opção Carregando")
            case 2:
                print("opção Carregando")
            case 3:
                print("opção Carregando")
            case 4:
                print("opção Carregando")
            case 0:
                print("🏦 Voltando à Agência..."); break
            case _:
                print(f"{Cores.Red_Ligth}❗ Apenas Números... 😃{Cores.Reset}")