# 💾 Arquivos Importados
import Classe
import Tabela
import Verifica
import Cores


def New_Cad():
    print("\nPreencha com suas Informações...")
    
    while True:
        try:
            Nome = Verifica.Verifica_String("Nome")
            SobreNome = Verifica.Verifica_String("SobreNome")
            Idade = Verifica.Verificar_Idade("Idade")
            Senha = Verifica.Verificar_Senha("Senha")
        except ValueError:
            print(f"{Cores.Red_Ligth}❗ Erro... 🤨 no Cadastro{Cores.Reset}")
            continue
            
        New_CL = Classe.Cla_CT(Nome, SobreNome, Idade, Senha)
        Tabela.Contas_Criadas.append(New_CL)
        
        for CL in Tabela.Contas_Criadas:
            if CL.Get_Nome()== Nome and CL.Get_SobreNome() == SobreNome:
                print("Cliente já Cadastrado...")
                return
            
        
        print("Cadastrado com Sucesso...")
        print(f"Número da Conta Gerado: {New_CL.Get_Num()}")
        print(f"Detalhes: \n{New_CL.Info_User()}")
        
        input("Pressione ENTER para voltar ao Menu...")
        break
        