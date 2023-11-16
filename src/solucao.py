import instancia
import time


'''
Restrições Fortes:
– H1-Aulas: Todas as aulas de uma disciplina devem ser alocadas, e em períodos
diferentes. Uma violação ocorre se uma aula não é alocada, ou se duas aulas da
mesma disciplina são alocadas no mesmo período.
– H2-Ocupação de Sala: Duas aulas não podem ser alocadas em uma mesma sala
e no mesmo período. Cada aula extra em uma mesma sala e no mesmo período
conta como uma violação.
– H3-Conflitos: Aulas de disciplinas de um mesmo currículo, ou ministradas
pelo mesmo professor devem ser alocadas em períodos diferentes. Duas aulas
conflitantes no mesmo período representa uma violação.
– H4-Indisponibilidade: Se o professor de uma disciplina não está disponível para
lecioná-la em determinado período, nenhuma aula dessa disciplina pode ser
alocada nesse período. Cada aula alocada em um período não disponível para a
disciplina conta como uma violação.
• Restrições Fracas:
– S1-Capacidade de Sala: Para cada disciplina, o número de alunos que está
matriculado na disciplina deve ser menor ou igual ao número de assentos
disponíveis em todas as salas que ocorrem aulas dessa disciplina. Cada aluno
acima da capacidade conta como uma violação.
– S2-Número Mínimo de Dias de Aula: As aulas de uma disciplina devem ser
espalhadas em um número mínimo de dias. Cada dia abaixo do número mínimo
de dias conta como uma violação.
– S3-Aulas Isoladas: Aulas de disciplinas de um mesmo currículo devem ser
adjacentes uma à outra. Para cada currículo, uma violação é contada quando há
uma aula não adjacente à nenhuma outra aula do mesmo currículo no mesmo
dia.
– S4-Estabilidade de Sala: Todas as aulas de uma disciplina devem acontecer
na mesma sala. Cada sala distinta usada para aulas dessa disciplina, além da
primeira, contam como uma violação.
'''

class Solucao(instancia.Instancia):
    def __init__(self, timelimit):
        self.timelimit = timelimit
        self.le_instancia() # herdado da classe instancia
        print(self.str_Instancia()) 
        
        self.matriz_alocacao = self.inicializaMatrizAlocacao()
        self.custo = 0
        
        self.solucao_inicial = self.geraSolucaoInicial()
        self.melhor_solucao = solucao
        
        #self.solucao_atual = self.geraSolucaoInicial()
        #self.melhor_solucao = self.solucao_atual
        #self.melhor_custo = self.calculaCusto(self.melhor_solucao)

    def inicializaMatrizAlocacao(self):
        matriz_alocacao = []
        for i in range(self.qtd_salas):
            sala = []
            matriz_alocacao.append(sala)
            for j in range(self.qtd_dias):
                dia = []
                matriz_alocacao[i].append(dia)
                for k in range(self.qtd_horarios):
                    matriz_alocacao[i][j].append(-1)
        
        return matriz_alocacao
    
    def __str__(self):
        # imprimir a partir de self.best_solution
        string = self.str_Solucao()

        return string
    
    def str_Solucao(self):
        string = "Solucao: \n"
        for i in range(self.qtd_salas):
            for j in range(self.qtd_dias):
                for k in range(self.qtd_horarios):
                    if self.matriz_alocacao[i][j][k] != -1:
                        string += f"{self.lista_cursos[self.matriz_alocacao[i][j][k]].nome} {self.lista_salas[i].nome} {j} {k}\n"
        return string

    def str_Matriz_Alocacao(self):
        string = ""
        for i in range(self.qtd_salas):
            string += f"{self.lista_salas[i]}\n"
            for j in range(self.qtd_dias):
                for k in range(self.qtd_horarios):
                    if self.matriz_alocacao[i][j][k] == -1:
                        string += "Vazio "
                    else:
                        string += f"{self.lista_cursos[self.matriz_alocacao[i][j][k]].nome} "
                    #string += str(self.matriz_alocacao[i][j][k]) + " "
                string += "\n"
        return string
            
    def geraSolucaoInicial(self):
        solucao = self.matriz_alocacao
        
        for c in range(self.qtd_cursos):
            for qtd in range(self.lista_cursos[c].qtd_aulas):
                alocado = 0
                for i in range(self.qtd_dias):
                    if alocado == 1: break
                    for j in range(self.qtd_horarios):
                        if alocado == 1: break
                        for k in range(self.qtd_salas):
                            if alocado == 1: break
                            if solucao[k][i][j] == -1: # verifica se a sala nesse dia e horario esta vago
                                if True: #verificar se o horario i j nao é proibido do curso 
                                        #esse check deve ver as restricoes de professor
                                    solucao[k][i][j] = c 
                                    alocado = 1
        
        return solucao
                                
                                
                                    


    def verificaDisponibilidade(self, i, j):
        if self.matriz_alocacao[i][j] == None: # Verifica se nenhuma aula foi alocada
            # fazer verificacao se nao esta dentro da lista de indisponibilidades
            return 1
        
        return 0

    def lns(self):
        while time.time() < self.timelimit:
            self.destroy(self.solucao_atual)
            #destroy solucao
            #repair solucao
            
            #avalia
                #melhor solucao = solucao
            
    def lns_destroy(self, solucao):
        solucao_destruida = solucao
        lista_removidos = []
        
        # VASCULHAS ENTRE AS SALAS DIAS E HORARIOS PROCURANDO QUAIS TEM UM GRANDE IMPACTO


        #remover 15 % dos alocados
        
        return solucao_destruida, lista_removidos
    
    def lns_repair(self, solucao_destruida, lista_removidos):
        while lista_removidos != vazio:            
            insere 
        
        

    def verificaValidadeSolucao(self):
        validade = 1
        validade -= self.restricao_1()
        validade -= self.restricao_2()
        validade -= self.restricao_3()
        validade -= self.restricao_4()
        return validade
        
    def calculaCusto(self, solucao):
        custo = 0
        custo += 1 * self.restricao_5(solucao)
        custo += 5 * self.restricao_6(solucao)
        custo += 2 * self.restricao_7(solucao)
        custo += 1 * self.restricao_8(solucao)
        return custo
                
    
    def restricao_1(self):
        return 0
    def restricao_2(self): 
        return 0
    def restricao_3(self):
        return 0
    def restricao_4(self):
        return 0
    def restricao_5(self):
        return 0
    def restricao_6(self):
        return 0
    def restricao_7(self):
        return 0
    def restricao_8(self):
        return 0
