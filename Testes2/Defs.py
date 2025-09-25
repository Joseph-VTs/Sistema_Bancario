import Valida
import datetime
import os

def Limpar_Terminal():
    return os.system('cls' if os.Name == 'nt' else 'clear')

def Criar_Barras(): # Criar Barras para Estilo
    return print("-" * 32)

Data = datetime.datetime.now()
Dia = Data.day
Mes = Data.month
Ano = Data.year

def Cadastro():
    return "Cadastros"

def Mostrar_Dados():
    return "Mostrar Dados"

def Relatorio():
    return "Relatórios"
