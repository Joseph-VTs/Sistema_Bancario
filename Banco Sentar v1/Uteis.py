# 💾 Arquivos Importados
import Cores
import os

def Limpar_Terminal():
    while True:
        Resposta = input(f"❗ Aperte {Cores.Yellow_Ligth}Enter{Cores.Reset} Para Continuar: ")
        if Resposta == '':
            break
        else:
            print(f"{Cores.Red_Ligth}❌ Apenas Aperte Enter... 🙂{Cores.Reset}")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
import random
#Gerador de Conta Aleatória
def Random_Conta():
    return f"{random.randint(0, 999999):06d}"