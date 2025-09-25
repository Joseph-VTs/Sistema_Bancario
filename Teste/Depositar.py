# Importar Outros Arquivos
import Cores

def Executar():
    Valor = int(input("Digite: "))
    
    return Cores.Print_Color(
        Cores.Green + "✅ Déposito foi Realizado", " ",
        Cores.Reset + "R$:", " ", f"{Valor:.2f}"
    )