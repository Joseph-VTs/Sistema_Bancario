# 💾 Arquivos Importados
import Cores
import Uteis
import Verifica
import Tabela
import Cadastro
import Classe

def Iniciar():
    while True:
        Uteis.Limpar_Terminal()
        
        print("=" * 50)
        print(f"{Cores.Ciano}🏦 Banco Sentar.{Cores.Reset}")
        print("Seja Bem-Vindo á Agência...")
        print("-" * 50)
        print(f"[{Cores.Ciano_Ligth}1{Cores.Reset}] 🆕 - Cadastrar-Se")
        print(f"[{Cores.Ciano_Ligth}2{Cores.Reset}] 👤 - Entrar")
        print(f"[{Cores.Ciano_Ligth}3{Cores.Reset}] 📄 - Tabela de Clientes")
        print(f"[{Cores.Ciano_Ligth}4{Cores.Reset}] 📄 - Carregar")
        print(f"[{Cores.Ciano_Ligth}0{Cores.Reset}] 🔐 - 👋 Sair...")
        print("=" * 50)
        
        try:
            Options_Menu = int(input(f"{Cores.Black}💢 Escolha uma Opção:{Cores.Reset} "))
        except ValueError:
            print(f"{Cores.Red_Ligth}❗ Essa não é uma Opção... 😀{Cores.Reset}")
            continue
        
        match Options_Menu:
            case 0: 
                print("Saindo... Volte Sempre que quiser Descançar..."); break
            case 1: 
                Cadastro.New_Cad()
            case 2: 
                Verifica.Verificar_Cadastro()
            case 3:
                Tabela.Clientes_Cad(Tabela.Contas_Criadas)
            case _: 
                print(f"{Cores.Yellow_Ligth}❗ Não Temos Essa Opção... 🙃{Cores.Reset}")

if __name__ == '__main__':
    Iniciar()