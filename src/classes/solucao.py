import instancia

class Solucao(instancia.Instancia):
    def __init__(self):
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

    def geraSolucaoInicial(self):
        for curso in self.lista_cursos:
            alocado = 0
            i = 0; j = 0
            while not alocado:
                if self.verificaDisponibilidade(i, j):
                    self.matriz_alocacao[i][j] = curso
                    alocado = 1
        
        self.validade = self.verificaValidadeSolucao()
        self.custo = self.calculaCusto()
            
    def verificaDisponibilidade(self, i, j):
        if self.matriz_alocacao[i][j] == None: # Verifica se nenhuma aula foi alocada
            # fazer verificacao se nao esta dentro da lista de indisponibilidades
            return 1
        
        return 0

    def verificaValidadeSolucao(self):
        validade = 1
        validade -= self.restricao_1()
        validade -= self.restricao_2()
        validade -= self.restricao_3()
        validade -= self.restricao_4()

    def calculaCusto(self):
        custo = 0
        custo += restricao_5()
        custo += restricao_6()
        custo += restricao_7()
        custo += restricao_8()
        return custo
                
    
    def restricao_1(self):
        
    def restricao_2(self):
        
    def restricao_3(self):
        
    def restricao_4(self):
    
    def restricao_5(self):
        
    def restricao_6(self):
        
    def restricao_7(self):
        
    def restricao_8(self):
    
    
    
s = Solucao(4, 3)
print(s)