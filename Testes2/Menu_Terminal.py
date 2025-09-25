# Cores
Ciano_Claro = '\033[1;96m'
Azul_Claro = '\033[1;36m'
Reset = '\033[0m'
Red = '\033[1;31m'
Green = '\033[1;32m'
Blue = '\033[1;34m'

Blue_Italico = '\033[3;44m'

#Variaveis
Nick = "Joseph"

def Menu_Terminal():
    while True:
        print(f"{'=' * 50}")
        print(f"<<< 🏧 {Ciano_Claro}Banco Sentar{Reset} >>> Seja Bem-Vindo {Green}{Nick}{Reset}".center(50))
        print(f"{'=' * 50}")
        print(f"{Blue_Italico} Opções do Terminal {Reset}")
        print()
        print(f"| [{Azul_Claro}1{Reset}] - 📄 - Extratos")
        print(f"| [{Azul_Claro}2{Reset}] - 📤 - Saque")
        print(f"| [{Azul_Claro}3{Reset}] - 📥 - Depósito")
        print(f"| [{Azul_Claro}4{Reset}] - 🔁 - Tranferências")
        print(f"| [{Azul_Claro}0{Reset}] - 🔐 Encerrar Sessão...")
        print(f"{'=' * 50}")
        
        try:
            Optinos_Menu = int(input("💢 Menu Digite uma Opção: ").strip())
        except ValueError:
            # Trata Erros -> Letra, Espaços, Simbolos
            print(f"{Red}❌ Opção Inválida!{Reset}")
            continue
        
        if Optinos_Menu == 0:
            print(f"🔐 {Blue}Encerrando Sessão...{Reset}")
            break
        elif Optinos_Menu == 1:
            print("1")
            
        elif Optinos_Menu == 2:
            print("2")
            
        elif Optinos_Menu == 3:
            print("3")
            
        elif Optinos_Menu == 4:
            print("4")
            
        else:
            # Númeos Negativos e Números Inválidos
            print(f"{Red}❌ Opção Inválida!{Reset}")
            
        
Menu_Terminal()