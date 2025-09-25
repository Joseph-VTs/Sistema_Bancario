# Importar Outros Arquivos
import Cores

def Valida_Terminal(Entrada, Options_Validas):
    try:
        Numero = int(Entrada.strip())
        if Numero < 0:
            Cores.Print_Color(Cores.Red + "❌ Número Negativo...")
            return None
        elif Numero not in Options_Validas:
            Cores.Print_Color(Cores.Red + "❌ Opção Não Existe.")
            return None
        return Numero
    except ValueError:
        Cores.Print_Color(Cores.Red + "❌ Digite Apenas Números!")
        return None
 



""" # Primeira Tentaic
def Valida_Terminal():
    try:
        Options_Menu = ""
        Options_Menu_Validas = []
        if Options_Menu not in Options_Menu_Validas:
            print("\033[1;31m❌ Opção inexistente. Tente novamente.\033[0m")
    except ValueError:
        print("❌ Número Negativo.")    
"""
