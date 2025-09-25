import Valida
import datetime
import os

#Variaveis
Red = '\033[1;31m'
Green = '\033[1;32m'
Yellow = '\033[1;33m'
Blue = '\033[1;34m'
Ciano = '\033[1;36m'

Green_Ligth = '\033[1;92m'
Ciano_Ligth = '\033[1;96m'
Reset = '\033[0m'
Bold = '\033[1m'


def Limpar_Terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def Criar_Barras():
    return print("-" * 32)

Data = datetime.datetime.now()
Dia = Data.day
Mes = Data.month
Ano = Data.year

def Menu():
    print(f"========{Blue} 🏧 Banco Sentar {Reset}========")
    print(f"| [{Ciano_Ligth}1{Reset}] Cadastrar Cliente         |")
    print(f"| [{Ciano_Ligth}2{Reset}] Dados do Cliente          |")
    print(f"| [{Ciano_Ligth}3{Reset}] Mostrar Clientes          |")
    print(f"| [{Ciano_Ligth}4{Reset}] Gerar Relatório           |")
    print(f"| [{Ciano_Ligth}0{Reset}] Sair                      |") 
    print('-------------------------')
    x = input(f"{Ciano}💢 Insira uma Opção{Reset}: ")
    print('-------------------------')
    return x

def Cadastro():
    Limpar_Terminal()
    print(f"===== < {Green_Ligth}Cadastrar Usuário{Reset} > =====")
    Nome = Valida.Nome()
    SobreNome = Valida.SobreNome()
    Login = Valida.Login()
    
    #Conferir Cadastro
    Ler_Logins = open('Logins.txt', 'r')
    for Linha in Ler_Logins.readlines():
        Valores = Linha.split('-')
        
        if Login == Valores[2].split(':')[2].strip():
            Limpar_Terminal()
            Criar_Barras()
            print(f"{Red}❗ Login já Existe...{Reset}")
    Ler_Logins.close()
    
    Senha = Valida.Senha()
    Data = Valida.Data()
    Telefone = Valida.Telefone()
    
    Limpar_Terminal()
    Criar_Barras()
    print(f"{Green}✅ Cadastro com Sucesso...{Reset}")
    Criar_Barras()
    
    Logins = open("logins.txt", "a")
    Logins.write(
        f"\n{Green}✅ Casdastrado...{Reset}",
        f"\nNome: {Nome}",
        f"\nSobreNome: {SobreNome}",
        f"\nLogin de Usuário: {Login}",
        f"\nSenha do Usuário: {Senha}",
        f"\nData de Nascimento: {Data}",
        f"\nNúmero de Telefone: {Telefone}"
    )
    Logins.close()
    return
    
def Mostra_Dados():
    
    Limpar_Terminal()
    print(f"===== <<< {Yellow}📄 Dados do Cliente{Reset} >>> =====")
    Criar_Barras()
    print(f"{Red}❗ Logue para Acessar seus Dados{Reset}")
    Criar_Barras()
    
    User_Login = input("Login: ")
    User_Senha = input("Senha: ")
    
    Valida = False
    
    Logins = open('Logins.txt', 'r')
    for Linha in Logins.readlines():
        Valores = Linha.split('-')
        
        if User_Login == Valores[2].split(':')[2].strip() and User_Senha in Valores[3].split(':')[3].strip():
            Limpar_Terminal()
            Criar_Barras()
            print(f"{Green}✅ Cliente Logado!{Reset} Dados do Usuário: ")
            Criar_Barras()    
    if not Valida:
        Limpar_Terminal()
        Criar_Barras()
        print(f"{Red}❌ Login ou Senha Inválido!!!{Reset}")
        Criar_Barras()
        
def Clientes_Cadastrados():
    
    Limpar_Terminal()
    print(f"===== <<< {Yellow}📄 Clientes Cadastrado{Reset} >>> =====")
    Logins = open('Logins.txt', 'r')
    for Linhas in Logins.readlines():
        L = Linhas.split('-')
        print(f"{Green_Ligth}{L[0]} | {L [2]}{Reset}")
    Criar_Barras()
    return
    
def Relatorios():
    Count_Clientes = 0
    Nomes = []
    
    Logins = open('Logins.txt', 'r')
    for Linhas in Logins.readlines():
        L = Linhas.split('-')
        Nomes.append(L[0])
        Count_Clientes +=1
        
    Limpar_Terminal()
    Arquivo = open("Dados.txt", "w+")
    Arquivo.write(f"{Yellow}📄 Relatório de Clientes{Reset} \n")
    Arquivo.write("\n")
    Arquivo.write(f"{Blue}🏦 O Banco Sentar{Reset} -> Possui {Bold}{Count_Clientes:.0f}{Reset} Cliente(s) \n")
    
    for i in range(len(Nomes)):
        Arquivo.write(str(f"{i + 1}.{Nomes[i].split(":")[1]} \n"))
        
    Arquivo.write(f"Data: {Dia}/{Mes}/{Ano}.")
    Criar_Barras()
    print(f"{Green}✅ Relatório Gerado em{Reset} {Bold}Dados.txt{Reset}")
    Criar_Barras()
    Arquivo.close()
    return