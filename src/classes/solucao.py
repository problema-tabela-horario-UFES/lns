#from instancia import *

class Solucao:
    def __init__(self, dias=1, horarios=1):
        self.dias = dias
        self.horarios = horarios
        
        self.custo = 0
        
        self.matriz_alocacao = []

        for i in range(self.dias):
            dia = []
            self.matriz_alocacao.append(dia)
            for j in range(self.horarios):
                #print(i + j)
                self.matriz_alocacao[i].append(i+j)
                
    
    def __str__(self):
        string = ""
        for i in range(self.dias):
            for j in range(self.horarios):
                string += str(self.matriz_alocacao[i][j]) + " "
            string += "\n"
            
        return string
    
s = Solucao(4, 3)
print(s)