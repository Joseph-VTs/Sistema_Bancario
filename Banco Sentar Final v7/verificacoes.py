# verificacoes.py

import config as Cores # Importa as cores como 'Cores'
from config import Notas_Aceitas # Importa as Notas_Aceitas

# -------------------
# Notas Aceitas
# -------------------

def Combinar(Valor, Notas):
    if Valor == 0:
        return True
    if Valor < 0:
        return False
    for Nota in Notas:
        if Combinar(Valor - Nota, Notas):
            return True
    return False

def Valor_Validado(Valor, Notas):
    if Valor <= 0:
        return False
    # A função Combinar utiliza as notas
    return Combinar(Valor, Notas) 

# -------------------
# Verificação de Entrada de Strings (Validação)
# -------------------
def Ver_Str(Texto="Texto do Input"):
    
    while True:
        try:
            Entrada = input(f"{Texto}: ").strip()
        except ValueError:
            # Usa Cores.Yellow e Cores.Reset
            print(f"{Cores.Yellow}❗ Entrada Inválida. Por Favor Tente Novamente.{Cores.Reset}")
            continue
        
        if Entrada.lower() == "sair":
            # Usa Cores.Yellow_Ligth e Cores.Reset
            print(f"{Cores.Yellow_Ligth}❗ Operação cancelada pelo usuário.{Cores.Reset}")
            return None
        
        if not Entrada:
            # Usa Cores.Red_Ligth e Cores.Reset
            print(f"{Cores.Red_Ligth}{Texto} ❌ Não Pode ser Vazio...{Cores.Reset}")
            continue
        
        if not Entrada.replace(" ", "").isalpha():
            # Usa Cores.Red_Ligth e Cores.Reset
            print(f"{Cores.Red_Ligth}{Texto} ❌ Deve Conter Apenas Letras...{Cores.Reset}")
            continue
        
        return Entrada
    
# Verificação de Entrada da Idade (Validação)
def Ver_Idade():
    
    while True:
    
        try:
            Entrada = input("Digite sua Idade: ").strip()
        except ValueError:
            # Usa Cores.Yellow e Cores.Reset
            print(f"{Cores.Yellow}❗ Entrada Inválida. Por Favor Tente Novamente.{Cores.Reset}")
            continue
        
        if Entrada.lower() == "sair":
            # Usa Cores.Yellow_Ligth e Cores.Reset
            print(f"{Cores.Yellow_Ligth}❗ Operação cancelada pelo usuário.{Cores.Reset}")
            return None
        
        if not Entrada.isdigit():
            # Usa Cores.Yellow_Ligth e Cores.Reset
            print(f"{Cores.Yellow_Ligth}❗ Idade Deve ser um Número Inteiro e Positivo...{Cores.Reset}")
            continue
        
        Convert = int(Entrada)
        
        if Convert < 0:
            # Usa Cores.Yellow_Ligth e Cores.Reset
            print(f"{Cores.Yellow_Ligth}❗ Idade não pode ser um Número Negativo...{Cores.Reset}")
            continue
            
        if Convert < 18:
            # Usa Cores.Yellow_Ligth e Cores.Reset
            print(f"{Cores.Yellow_Ligth}❗ Menor de Idade...{Cores.Reset}")
            print("Lamentamos, porém menores de Idade não Podem fazer seu Cadastro. Volte quando tiver seus 18 anos ou mais")
            return None
            
        if Convert > 120:
            # Usa Cores.Yellow_Ligth e Cores.Reset
            print(f"{Cores.Yellow_Ligth}❗ Idade Inválida...{Cores.Reset}")
            return None
        
        # Usa Cores.Green_Ligth e Cores.Reset
        print(f"{Cores.Green_Ligth}✅ Salvo...{Cores.Reset}")
        return Convert
  
   
# Verificação de Entrada da Senha (Validação)
def Ver_Senha():
    while True:
        Entrada = input("Digite a Senha (4 Dígitos) ou 'sair' para cancelar: ").strip()

        if Entrada.lower() == "sair":
            # Usa Cores.Yellow_Ligth e Cores.Reset
            print(f"{Cores.Yellow_Ligth}❗ Operação cancelada pelo usuário.{Cores.Reset}")
            return None

        if not Entrada.isdigit():
            # Usa Cores.Yellow_Ligth e Cores.Reset
            print(f"{Cores.Yellow_Ligth}❗ Senha deve conter apenas números.{Cores.Reset}")
            continue

        if len(Entrada) != 4:
            # Usa Cores.Yellow_Ligth e Cores.Reset
            print(f"{Cores.Yellow_Ligth}❗ Senha deve ter exatamente 4 dígitos.{Cores.Reset}")
            continue

        # Usa Cores.Green_Ligth e Cores.Reset
        print(f"{Cores.Green_Ligth}✅ Senha salva com sucesso!{Cores.Reset}")
        return Entrada
    
    
# Verificação de Entrada da Depósito Agência (Validação)
def Ver_Float():
 
    while True:
        Entrada = input("Digite um Valor R$ (ou digite 'sair' para cancelar): ").strip().replace(",", ".")

        if Entrada.lower() == "sair":
            # Usa Cores.Yellow_Ligth e Cores.Reset
            print(f"{Cores.Yellow_Ligth}❗ Operação cancelada pelo usuário.{Cores.Reset}")
            return None

        if Entrada.isalpha():
            # Usa Cores.Yellow_Ligth e Cores.Reset
            print(f"{Cores.Yellow_Ligth}❗ Não pode ser Letras ou Símbolos.{Cores.Reset}")
            continue

        try:
            Value_Convert = float(Entrada)
        except ValueError:
            # Usa Cores.Yellow e Cores.Reset
            print(f"{Cores.Yellow}❗ Entrada Inválida. Por Favor Tente Novamente.{Cores.Reset}")
            continue

        if Value_Convert <= 0:
            # Usa Cores.Yellow_Ligth e Cores.Reset
            print(f"{Cores.Yellow_Ligth}❗ O Valor deve ser Maior que Zero.{Cores.Reset}")
            continue

        return Value_Convert