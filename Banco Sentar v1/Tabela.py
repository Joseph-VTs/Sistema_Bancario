# 💾 Arquivos Importados
import Cores


# Guarda Clientes
Contas_Criadas = []



def Clientes_Cad(Clientes):
    # Cabeçalho
    print("-" * 40)
    print(f"| {Cores.Blue_Ligth}{'Cod':<5}{Cores.Reset} | {Cores.Blue_Ligth}{'Nome':<10}{Cores.Reset} | {Cores.Blue_Ligth}{'SobreNome':<15}{Cores.Reset} | {Cores.Blue_Ligth}{'Idade':<5}{Cores.Reset} |")
    print("-" * 40)
    # Conteúdo
    for i, Cliente in enumerate(Clientes):
        print(f"| {i + 1:<5} | {Cliente.Get_Nome():<10} | {Cliente.Get_SobreNome():<15} | {Cliente.Get_Idade():<5} |")
    print("-" * 40)
    print(f"O Banco Sentar Possui {Cores.Italico}{len(Contas_Criadas)}{Cores.Reset} Cadastrados...")
    
def Lista_Clientes():
    if not Contas_Criadas:
        print(f"{Cores.Red_Ligth}❗ Nenhuma Conta Cadastrada{Cores.Reset}")
        return
    
    print("\n----- Contas Cadastradas -----")
    for i, Conta in enumerate(Contas_Criadas):
        print(f"[{i + 1}] - {Conta}")
    print("--------------------------------")
    