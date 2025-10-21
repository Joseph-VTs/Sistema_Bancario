# main.py

import config as Cores # Importa as cores como 'Cores'
import uteis as Uteis
import interface as Interface

def Iniciar():
    while True:
        Uteis.Limpar_Terminal()
        
        print("=" * 50)
        # Usa Cores.Ciano e Cores.Reset
        print(f"{Cores.Ciano}🏦 Banco Sentar.{Cores.Reset}")
        print(f"Seja Bem-Vindo á Agência...")
        print("-" * 50)
        
        # Opções de Menu
        print(f"[{Cores.Ciano_Ligth}1{Cores.Reset}] 👤 - Entrar")
        print(f"[{Cores.Ciano_Ligth}2{Cores.Reset}] 🆕 - Cadastrar-Se")
        print(f"[{Cores.Ciano_Ligth}3{Cores.Reset}] 📄 - Lista de Clientes")
        print(f"[{Cores.Ciano_Ligth}4{Cores.Reset}] 📄 - Manual do Usuário")
        print(f"[{Cores.Ciano_Ligth}0{Cores.Reset}] 🔐 - 👋 Sair...")
        print("=" * 50)
        
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
                print("Saindo... Volte Sempre que quiser Descançar..."); break
            case 1:
                Interface.Processar_Login()
            case 2:
                Interface.Processar_Cadastro()
            case 3:
                Uteis.Lista_Clientes()
                Uteis.Limpar_Terminal()
            case 4:
                Uteis.Mostrar_Manual()
                Uteis.Limpar_Terminal()
            case _: 
                # Usa Cores.Yellow_Ligth e Cores.Reset
                print(f"{Cores.Yellow_Ligth}❗ Não Temos Essa Opção... 🙃{Cores.Reset}")
                Uteis.Limpar_Terminal()

if __name__ == '__main__':
    Iniciar()