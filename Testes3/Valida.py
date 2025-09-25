import Defs

def Nome():
    while True:
        Nome = input("Nome: ")   
        if Nome == '' :
            print(f"{Defs.Red}❌ Entrada Vazia...{Defs.Reset}")
            continue
        Temp = ''.join(Nome.split(' '))
        
        for i in Temp:
            if i.isdigit():
                print(f"{Defs.Red}❌ Digite um Nome Válido.{Defs.Reset}")
                break
        else:
            return Nome.strip(' ')

def SobreNome():
    while True:
        SobreNome = input("SobreNome: ")   
        if SobreNome == '' :
            print(f"{Defs.Red}❌ Entrada Vazia...{Defs.Reset}")
            continue
        Temp = ''.join(SobreNome.split(' '))
        
        for i in Temp:
            if i.isdigit():
                print(f"{Defs.Red}❌ Digite um SobreNome Válido.{Defs.Reset}")
                break
        else:
            return SobreNome.strip(' ')
    
def Login():
    while True:
        Login = input("Login: ")
        
        if Login == '':
            print(f"{Defs.Red}❌ Entrada Vazia...{Defs.Reset}")
            continue
        return Login.strip(' ')
    
def Senha():
    while True:
        Senha = input("Senha: ")
        if Senha == '':
            print(f"{Defs.Red}❌ Entrada Vazia...{Defs.Reset}")
            continue
        return Senha.strip(' ')
    
def Data():
    while True:
        Data = input("Data de Nascimento (dd/mm/aaaa): ")
        
        if Data == '':
            print(f"{Defs.Red}❌ Entrada Vazia...{Defs.Reset}")
            continue
        
        Temp = ''.join(Data.split('/')) # Remove  a '/'
        
        if not Temp.isnumeric():
            print(f"{Defs.Red}❌ Insira uma Data Váilida.{Defs.Reset}")
            continue
        
        if Data.count('/') == 2 and Data != '//':
            Dia, Mes, Ano = Data.split('/')
            if 1 <= int(Dia) <= 31 and 1 <= int(Mes) <= 12 and 1900 <= int(Ano) <= 2025:
                return Data.strip(' ')
            else:
                print(f"{Defs.Red}❌ Dia/Mês/Ano -> Inválido(s).{Defs.Reset}")
        else:
            print(f"{Defs.Yellow}❗ Padrão da Data -> dd/mm/aaaa {Defs.Reset}")
            
def Telefone():
    while True:
        Cell = input("Celular: ")
        
        if Cell == '':
            print(f"{Defs.Red}❌ Entrada Vazia...{Defs.Reset}")
            continue
        elif not Cell.isnumeric():
            print(f"{Defs.Red}❗ Insira Apenas Números...{Defs.Reset}")
            continue
        else:
            if 9 <= len(Cell) <= 11:
                return Cell
            else:
                print(f"{Defs.Red}❗ Número deve ter entre 9 á 11 Caracteres.{Defs.Reset}")
                
            