import os

def Limpar_Terminal():
    return os.system('cls' if os.Name == 'nt' else 'clear')