# Cores 😀😯🙃
White = '\033[1;37m'
Blue = '\033[1;34m'
Red = '\033[1;31m'
Yellow = '\033[1;33m'
Green = '\033[1;32m'

#Fundos
Fundo_White = '\033[7;37m'
Fundo_Blue = '\033[7;34m'
Fundo_Red = '\033[7;31m'
Fundo_Yellow = '\033[7;33m'
Fundo_Green = '\033[7;32m'


# Efeitos de Textos
Reset = '\033[0m'
Bold = '\033[1m'
Italico = '\033[3m'
Underline = '\033[4m'
Reverse = '\033[7m'
Riscado = '\033[9m'

# Erro Caso Aplique com Múltiplas Cores
#def Print_Color(Texto, Cor = Reset):
#    print(f"{Cor}{Texto}\033[0m")
    
    
# A função junta tudo com "".join(...) e aplica o Reset no final. Isso permite misturar cores em uma única linha sem complicação  
def Print_Color(*Partes, end = "\n"):
    print("".join(Partes) + Reset, end = end)