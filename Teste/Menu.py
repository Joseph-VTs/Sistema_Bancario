# print("Aqui será a Tela do Terminal")

def Menu_Terminal():
    while True:
        print("-" * 41)
        print("Menu do Terminal: \"Senta, Senta que é Banco\"...")
        print("-" * 41)
        print()
        print("Opções:")
        print("[1] - Extrato Carão Crédito")
        print("[2] - Extrato Cartão Débito")
        print("[3] - Sacar sem Cartão")
        print("[4] - Sacar com Cartão")
        print("[5] - Depositar na Conta")
        print("[6] - Transferência Entre Contas")
        print("[7] - Recarga de Celular")
        print("[0] - Encerrar Sessão...")
        print("-" * 41)
        
        Option_Terminal = int(input("Escolha uma Opção: "))
        
        if Option_Terminal == 0:
            print("🔒 Encerrando Sessão...")
            break
        elif Option_Terminal == 1:
            print("Menu: 📄 Extrato do Cartão de Crédito:")
            print("-" * 40)            
        elif Option_Terminal == 2:
            print("Menu: 📄 Extrato do Cartão de Débito:")
            print("-" * 40)
        elif Option_Terminal == 3:
            print("Menu: 💸 Sacar sem Cartão:")
            print("-" * 40)
        elif Option_Terminal == 4:
            print("Menu: 💳 Sacar com Cartão:")
            print("-" * 40)
        elif Option_Terminal == 5:
            print("Menu: 📥 Depositar na Conta:")
            print("-" * 40)
            
            import Depositar
            Depositar.Executar()
        elif Option_Terminal == 6:
            print("Menu: 🔁 Transferência Entre Contas")
            print("-" * 40)
        elif Option_Terminal == 7:
            print("Menu: 📱 Recarga de Celular")
            print("-" * 40)
        else:
            print("❌ Opção inválida. Tente novamente...")

# Executar o Menu do Terminal
Menu_Terminal()