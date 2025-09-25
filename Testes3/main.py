import Defs

Defs.Limpar_Terminal()

while True:
    Escolha = Defs.Menu()
    
    if Escolha == '1':
        Defs.Cadastro()
    elif Escolha == '2':
        Defs.Mostra_Dados()
    elif Escolha == '3':
        Defs.Clientes_Cadastrados()
    elif Escolha == '4':
        Defs.Relatorios()
    elif Escolha == '0':
        print(f"{Defs.Ciano}🔐 Encerrando Sessão...{Defs.Reset}")
        break
    else:
        Defs.Limpar_Terminal()
        Defs.Criar_Barras()
        print(f"{Defs.Red}❌ Opção Inválida {Defs.Reset}")
        Defs.Criar_Barras()