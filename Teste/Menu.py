# Importar Outros Arquivos
import Validacoes
import Cores


Nick = "Joseph"

def Menu_Terminal():
    while True:
        # Menu de Opções
        print("=" * 40)
        Cores.Print_Color(
            Cores.Blue + "🏧 Banco Sentar.",
            Cores.Reset + " Seja Bem-Vindo ",
            Cores.Green + f"{Nick}..."
        )
        
        print("-" * 40)
        Cores.Print_Color(
            Cores.Blue + "[1]", Cores.Reset + " - 📄 Extratos",
            Cores.Blue + "\n[2]", Cores.Reset + " - 📤 Saque",
            Cores.Blue + "\n[3]", Cores.Reset + " - 📥 Depósito",
            Cores.Blue + "\n[4]", Cores.Reset + " - 🔁 Tranferência",
            Cores.Blue + "\n[0]", Cores.Reset + " - 🔒 Encerrar Sessão...",
        )
        print("=" * 40)
            
        # Entrada Menu
        # Options_Menu = Validacoes.Valida_Terminal(input("💢 Menu Digite uma Opção: "), [0, 1, 2, 3, 4])
        # if Options_Menu is None:
        #    continue
        
        Cores.Print_Color(Cores.Blue + "💢 Menu Digite uma Opção:", Cores.Reset, end=" ")
        Options_Menu = Validacoes.Valida_Terminal(input(), [0, 1, 2, 3, 4])

                      
        if Options_Menu == 0:
            print("💤 Encerrando Sessão...")
            break
        elif Options_Menu == 1: # + Sub Menu
            while True:
                print("=" * 40)
                print("📄 Extratos")
                print("-" * 40)
                print("[1] - 📄 Cartão de Crédito")
                print("[2] - 📄 Cartão de Débito")
                print("[0] - ↩ Voltar...")
                print("=" * 40)
                

                # Entrada Sub Menu
                Entrada = input("💢 SubMenu Digite uma Opção: ").strip()
                if not Validacoes.Valida_Terminal(Entrada, [0, 1, 2]):
                    continue
                Options_Menu = int(Entrada)
                
                
                if Options_Menu == 0:
                    # Volta para Options_Menu
                    print(" ⬅  Voltando...")
                    break
                elif Options_Menu == 1:
                    print("💾.py -> Detalhes do Extato")
                elif Options_Menu == 2:
                    print("💾.py -> Detalhes do Extato")        
        elif Options_Menu == 2:
            print("💾.py -> Sacar Valor....")
        elif Options_Menu == 3:
            print("💾.py -> Depósito \n")
            import Depositar # Outro Arquivo
            Depositar.Executar()

        elif Options_Menu == 4:
            print("💾.py -> Tranferências.....")
            continue
            
Menu_Terminal()