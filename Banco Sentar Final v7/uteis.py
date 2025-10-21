# uteis.py

import os
import random
from datetime import datetime
import config as Cores # Importa as cores como 'Cores'

def Limpar_Terminal():
    while True:
        # Usa Cores.Yellow_Ligth para a cor
        Resposta = input(f"❗ Aperte {Cores.Yellow_Ligth}Enter{Cores.Reset} Para Continuar: ") 
        if Resposta == '':
            break
        else:
            # Usa Cores.Red_Ligth e Cores.Reset
            print(f"{Cores.Red_Ligth}❌ Apenas Aperte Enter... 🙂{Cores.Reset}")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def Random_Conta():
    return f"{random.randint(0, 999999):06d}"

def Agora_hr():
    return datetime.now().strftime("%d/%m/%Y %H:%M")

def Mostrar_Manual():
    try:
        # Usa Cores.Ciano_Ligth e Cores.Red_Ligth
        with open("Manual.md", encoding="utf-8") as manual:
            print(f"{Cores.Ciano_Ligth}📘 Manual de Uso - Banco Sentar{Cores.Reset}")
            print("-" * 60)
            print(manual.read())
            print("-" * 60)
    except FileNotFoundError:
        print(f"{Cores.Red_Ligth}❌ Manual.md não encontrado no diretório.{Cores.Reset}")

def Lista_Clientes():
    # Importa a lista global de Contas_Criadas
    from config import Contas_Criadas

    if not Contas_Criadas:
        print(f"\n{Cores.Red_Ligth} Nenhuma Conta Encontrada...{Cores.Reset}")
        return
    
    print("\n----- Contas Cadastradas -----")
    # Usa Cores.Italico e Cores.Reset
    for i, conta in enumerate(sorted(Contas_Criadas, key=lambda c: c.Get_Titular())):
        print(f"[{i + 1}] - {conta.Get_Titular()}")
        print("-------------------------------------------")
    print(f"O Banco Sentar Possui {Cores.Italico}{len(Contas_Criadas)}{Cores.Reset} Clientes Cadastrados...")