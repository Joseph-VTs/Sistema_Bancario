# 💾 Arquivos Importados
import Cores
import Tabela
import Menu_Agencia
import Main
import Classe

# Verifica se Cliente está Cadastrado
def Verificar_Cadastro():
    print("\nPreencha com suas Informações")

    while True:
        try:
            Num_Conta = str(input("Número da Conta: "))
            Senha = str(input("Senha: "))
        except:
            print("Entrada Errada...")
            continue
        
        if not Tabela.Contas_Criadas:
            print("Não Cadastrada...")
            return
        
        Conta_Log = next((c for c in Tabela.Contas_Criadas if c.Get_Num() == Num_Conta), None)
        
        if Conta_Log:
            if Conta_Log.Get_Senha() == Senha:
                print(f"\n✅ Login bem-sucedido. Bem-vindo(a), {Conta_Log.Titular()}!")
                Main.Iniciar(Conta_Log) # Passa a conta logada para o Menu
                return # Sai da função Entrada
            else:
                print("❌ Senha incorreta.")
        else:
            print("❌ Conta não cadastrada.")
 

# Ideia da IA para não ficar Repetitivo
# Verificar se é uma String           
def Verifica_String(Campo: str) -> str:
    
    while True:
        try:
            Entrada = str(input(f"{Campo}: ").strip().title())
            if Entrada == '':
                print(f"{Cores.Yellow_Ligth}❗ Não pode ser Vazio... 😉{Cores.Reset}")
                continue
            elif Entrada.isalpha():
                if len(Entrada) >= 4:
                    print(f"{Cores.Green_Ligth}✔ Continue...{Cores.Reset}")
                    return Entrada # Trocado pelo Break
                else:
                    print(f"{Cores.Red_Ligth}❗ Nome deve ter pelo menos 4 Digítos... 😃{Cores.Reset}")
            else:
                print(f"{Cores.Red_Ligth}❗ Nome não pode ser Número ou Símbolo... 😐{Cores.Reset}")
        except ValueError:
            print(f"{Cores.Red_Ligth}❌ Apenas Letras... 😃{Cores.Reset}")
            
def Verificar_Idade(Campo: str) -> int:
    while True:
        try:
            Entrada = int(input(f"{Campo}: ").strip())
            
            if 18<= Entrada <= 120:
                print(f"{Cores.Green_Ligth}✔ Continue...{Cores.Reset}")
                return Entrada
            else:
                print(f"{Cores.Yellow_Ligth}❗ Idade deve estar entre 18 á 120... 🙃{Cores.Reset}")
        except ValueError:
            print(f"{Cores.Red_Ligth}❌ Apenas Números... 😃{Cores.Reset}")
            
def Verificar_Senha(Campo: str) -> str:
    while True:
        try:
            Entrada = str(input(f"{Campo}: ").strip())
            
            if Entrada == '':
                print(f"{Cores.Yellow_Ligth}❗ Senha não pode ser Vazia... 😉{Cores.Reset}")
            elif Entrada.isdigit():
                if len(Entrada) == 4:
                    return Entrada
                else:
                    print(f"{Cores.Red_Ligth}❗ Senha deve ter exatamente 4 Digítos... 🙃")
            else:
                print("Tipo de Erro")
        except ValueError:
            print(f"{Cores.Red_Ligth}❌ Apenas Números... 😃{Cores.Reset}")