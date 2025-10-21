# cliente.py

import verificacoes as Ver

# Classe do Cliente
class Cl_Cliente:
    # A classe cliente não precisa de Cores
    def __init__(self, Nome1, Nome2, Idade):
        self._Nome1 = Nome1
        self._Nome2 = Nome2
        self._Idade = Idade
       
    def Get_Nome1(self): return self._Nome1
    def Set_Nome1(self):
        New = Ver.Ver_Str("Digite seu Primeiro Nome")
        if New:
            self._Nome1 = New
    
    def Get_Nome2(self): return self._Nome2
    def Set_Nome2(self):
        New = Ver.Ver_Str("Digite seu Segundo Nome")
        if New:
            self._Nome2 = New
    
    def Get_Idade(self): return self._Idade
    def Set_Idade(self):
        New = Ver.Ver_Idade()
        if New:
            self._Idade = New
    
    # Nome e Sobrenome
    def Get_Titular(self): return f"{self.Get_Nome1()} {self.Get_Nome2()}"