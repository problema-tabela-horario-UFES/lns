import instancia
import time
import random
import copy

DEBUG = False
DEBUG_CUSTO = True

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
    def __init__(self):
        self.le_instancia() # herdado da classe instancia
        #print(self.str_Instancia()) 
        self.total_aulas = self.calculaTotalAulas() 
        

        self.matriz_alocacao = self.inicializaMatrizAlocacao()
        self.custo = 0
        
        self.solucao_inicial = self.geraSolucaoInicial()
        
        #print(self.calculaCusto(self.solucao_inicial))


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
    
    def str_Solucao(self, solucao):
        string = ""
        #string += "Solucao: \n"
        for i in range(self.qtd_salas):
            for j in range(self.qtd_dias):
                for k in range(self.qtd_horarios):
                    if solucao[i][j][k] != -1:
                        string += f"{self.lista_cursos[solucao[i][j][k]].nome} {self.lista_salas[i].nome} {j} {k}\n"
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
    
    def calculaTotalAulas(self):
        total = 0
        for c in range(self.qtd_cursos):
            total += self.lista_cursos[c].qtd_aulas
        
        return total

    def alocaCurso(self, curso, solucao, randomness):
        alocado = 0
        for k in range(self.qtd_salas):
            if alocado == 1: break
            for j in range(self.qtd_horarios):
                if alocado == 1: break
                for i in range(self.qtd_dias):
                    if alocado == 1: break
                    if random.random() < randomness: #fator de aleatoriedade 
                        if solucao[k][i][j] == -1:
                            if self.verificaDisponibilidade(solucao, curso, k, i, j): #verificar a disponibilidade de alocar o curso nessa sala dia horario
                                #print(self.lista_cursos[curso].nome, "alocado")
                                solucao[k][i][j] = curso
                                alocado = 1
        return solucao, alocado

    def alocaCursoForce(self, curso, solucao):
        #print("Force", self.lista_cursos[curso].nome)
        alocado = 0
        for k in range(self.qtd_salas):
            if alocado == 1: break
            for i in range(self.qtd_dias):
                if alocado == 1: break
                for j in range(self.qtd_horarios):
                    if alocado == 1: break
                    
                    if self.verificaDisponibilidade(solucao, curso, k, i, j) and solucao[k][i][j] != curso:
                        removido = solucao[k][i][j]
                        solucao[k][i][j] = curso
                        solucao, lixo = self.alocaCurso(removido, solucao, 1)
                        alocado = 1
        
        
        return solucao
    def geraSolucaoInicial(self):
        solucao = self.matriz_alocacao

        time_si = time.time()

        for c in range(self.qtd_cursos):
            for qtd in range(self.lista_cursos[c].qtd_aulas):
                solucao, alocado = self.alocaCurso(c, solucao, 0.2)
                if not alocado:
                    solucao, alocado = self.alocaCurso(c, solucao, 1)
                    if not alocado:
                        #print(self.lista_cursos[c].nome, "nao alocado")
                        solucao = self.alocaCursoForce(c, solucao)


        time_si = time.time() - time_si
        #print("Tempo Gerar Solucao Inicial:", time_si)
        return solucao
                                
                                
                                    


    def verificaDisponibilidade(self, solucao, curso, sala, dia, horario):
        if DEBUG: print("Verifica:", curso, sala, dia, horario)
        #if solucao[sala][dia][horario] != -1: # Sala nesse dia e horario esta ocupada
            #return 0

        # Verifica se o horario nao esta dentro da lista de indisponibilidades do curso
        for i in range(self.lista_cursos[curso].qtd_indisponibilidades):
            valor = self.lista_cursos[curso].lista_indisponibilidades[i]
            if int(dia) == int(valor[0]) and int(horario) == int(valor[1]):
                return 0
        
        # Verifica se o professor esta disponivel nesse horario
        for k in range(self.qtd_salas):
            if k != sala:
                if solucao[k][dia][horario] != -1:
                    #print( self.lista_cursos[curso], self.lista_cursos[ solucao[k][dia][horario] ])
                    if self.lista_cursos[curso].professor == self.lista_cursos[ solucao[k][dia][horario] ].professor:
                        #print("professor igual")
                        return 0
        
        # Verifica se alguma outra sala esta acontecendo aula dessa disciplina ou de alguma dentro do mesmo curriculo
        for cur in range(self.qtd_curriculos):
            if self.lista_cursos[curso].nome in self.lista_curriculos[cur].lista_disciplinas:
                for k in range(self.qtd_salas):
                    if k != sala:
                        if solucao[k][dia][horario] != -1:
                            #print(self.lista_cursos[ solucao[k][dia][horario] ].nome)
                            #print(self.lista_curriculos[cur].lista_disciplinas)
                            if self.lista_cursos[ solucao[k][dia][horario] ].nome in self.lista_curriculos[cur].lista_disciplinas:
                                return 0

                
        if int(self.lista_cursos[curso].qtd_alunos) > int(self.lista_salas[sala].capacidade):
            if random.random() > 0.75:
                return 0

        return 1

    def lns(self, timelimit):
        starttime = time.time()

        if DEBUG: print("Starttime", starttime)
        solucao = copy.deepcopy(self.solucao_inicial)
        custo = self.calculaCusto(solucao)
        if DEBUG: print("Custo inicial", custo)
        self.melhor_solucao = copy.deepcopy(solucao)

        while time.time() < starttime + timelimit:
            #print(custo)
            #print(time.time() - starttime)

            #print("ant", solucao)
            sol_des, remov = self.lns_destroy(copy.deepcopy(solucao))
            new_sol = self.lns_repair(sol_des, remov)
            #print("dep", solucao)

            #if random.random() < 0.15: # 15 perc chance att a solucao independente
            #    solucao = copy.deepcopy(new_sol)

            #print("comp\n", melhor_solucao, "\n x \n", new_sol)
            #print(, custo)
            #print(new_sol)
            avalia = self.calculaCusto(new_sol) 
            
            if avalia < custo:
                #print("melhora")
                solucao = copy.deepcopy(new_sol)
                self.melhor_solucao = copy.deepcopy(new_sol)
                #print("a\n", melhor_solucao, self.calculaCusto(melhor_solucao))
                custo = avalia
        
        if DEBUG_CUSTO:
            print("Custo Solucao Final:\n"); print(self.calculaCusto(self.melhor_solucao))

        return self.melhor_solucao
        #print("FIM LNS Solucao")
        #print(self.melhor_solucao, self.calculaCusto(self.melhor_solucao))


    def lns_destroy(self, solucao):
        if DEBUG: print("Destroy")
        solucao_destruida = solucao
        lista_removidos = []
        qtd_removidos = 0
        
        #print(self.total_aulas, self.total_aulas * 0.15)

        while qtd_removidos < self.total_aulas * 0.15:
            sala = random.randint(0, self.qtd_salas-1)
            dia = random.randint(0, self.qtd_dias-1)
            horario = random.randint(0, self.qtd_horarios-1)

            if solucao[sala][dia][horario] != -1:
                lista_removidos.append(solucao[sala][dia][horario])
                solucao[sala][dia][horario] = -1
                qtd_removidos += 1

        if DEBUG: print("removidos", lista_removidos)
        return solucao_destruida, lista_removidos
    
    def lns_repair(self, solucao_destruida, lista_removidos):
        if DEBUG: print("Repair")
        solucao = solucao_destruida
        while len(lista_removidos) > 0:
            curso = lista_removidos.pop()
            if DEBUG: print(curso)
            alocado = 0
            solucao, alocado = self.alocaCurso(curso, solucao, 0.2)
            if not alocado:
                solucao, alocado = self.alocaCurso(curso, solucao, 1)
                if not alocado:
                    solucao = self.alocaCursoForce(curso, solucao)
    
        return solucao

    def calculaCusto(self, solucao):
        custo = 0
        custo += self.restricao_5(solucao, 1)
        custo += self.restricao_6(solucao, 5)
        custo += self.restricao_7(solucao, 2)
        custo += self.restricao_8(solucao, 1)
        return custo
    
    def restricao_5(self, solucao, peso=1):
        custo = 0
        for k in range(self.qtd_salas):
            for i in range(self.qtd_dias):
                for j in range(self.qtd_horarios):
                    if solucao[k][i][j] != -1: # verifica se a sala nesse dia e horario esta vago
                        #avaliar qnts alunos tem a mais q a capacidade da sala 
                        if self.lista_cursos[solucao[k][i][j]].qtd_alunos > int(self.lista_salas[k].capacidade):
                            if DEBUG_CUSTO: print(self.lista_cursos[solucao[k][i][j]].nome, i , j ,self.lista_cursos[solucao[k][i][j]].qtd_alunos - int(self.lista_salas[k].capacidade))
                            custo += self.lista_cursos[solucao[k][i][j]].qtd_alunos - int(self.lista_salas[k].capacidade)
        if DEBUG_CUSTO: print("R5", custo*peso)
        return custo*peso
    
    def restricao_6(self, solucao, peso=5):
        # – S2-Número Mínimo de Dias de Aula: As aulas de uma disciplina devem ser espalhadas em um número mínimo de dias. Cada dia abaixo do número mínimo de dias conta como uma violação.
        custo = 0
        for c in range(self.qtd_cursos): # para cada curso
            
            qtd_dias = 0
            for i in range(self.qtd_dias):
                aux = 0
                for k in range(self.qtd_salas):
                    if aux == 1:
                        break
                    for j in range(self.qtd_horarios):
                        if solucao[k][i][j] == c:
                            aux = 1
                            break
                if aux == 1:
                    qtd_dias += 1
            
            if self.lista_cursos[c].num_min_dias > qtd_dias:
                if DEBUG_CUSTO: print(self.lista_cursos[c].nome, self.lista_cursos[c].num_min_dias, qtd_dias)
                custo += self.lista_cursos[c].num_min_dias - qtd_dias
        if DEBUG_CUSTO: print("R6", custo*peso)
        return custo * peso

    def restricao_7(self, solucao, peso=2):
        # CORRIGIR ESSE CALCULO
        
        custo = 0
        #– S3-Aulas Isoladas: Aulas de disciplinas de um mesmo currículo devem ser adjacentes uma à outra. Para cada currículo, uma violação é contada quando há uma aula não adjacente à nenhuma outra aula do mesmo currículo no mesmo dia.
        for k in range(self.qtd_salas):
            for i in range(self.qtd_dias):
                for cur in range(self.qtd_curriculos):
                    qtd = 0
                    seq = 0
                    max_seq = 0
                    for j in range(self.qtd_horarios):
                        if self.lista_cursos[ solucao[k][i][j] ].nome in self.lista_curriculos[cur].lista_disciplinas:
                            qtd += 1
                            seq += 1
                        else:
                            if seq > max_seq: max_seq = seq
                            seq = 0
                    
                    if qtd != max_seq:
                        custo += 1

        if DEBUG_CUSTO: print("R7", custo*peso)
        return custo*peso
    
    def restricao_8(self, solucao, peso=1):
        
        # as aulas de um curso devem ser na mesma sala
        custo = 0
        for c in range(self.qtd_cursos): # para cada curso verificar se ele esta na mesma sala
            sala = 0
            for k in range(self.qtd_salas):
                aux = 0
                for i in range(self.qtd_dias):
                    if aux == 1: 
                        break
                    for j in range(self.qtd_horarios):
                        if solucao[k][i][j] == c:
                            aux = 1
                            break

                sala += aux
            if DEBUG_CUSTO: print(self.lista_cursos[c].nome, sala)
            custo += sala - 1
        if DEBUG_CUSTO: print("R8", custo*peso)
        return custo*peso
