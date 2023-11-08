# Programa resolução do Problema de Tabela Horario para Universidades na formatação cbctt proposta pelo ITC 2007 utilizando a meta-heuristica Large Neighborhood Search

from solucao import *
from instancia import *
import time

timelimit = 144
starttime = time.time()

s = Solucao(starttime + timelimit)
print(s.str_Matriz_Alocacao())
print(s)

# solution = geraSolucaoInicial() #FAZER A FUNCAO DE GERAR SOLUCAO INICIAL
# best_solution = solution

# while actualtime < timelimit:
#     destroy_solution = lns_destroy(solution) # FAZER A FUNCAO DE DESTROY
#     new_solution = lns_repair(destroy_solution) # FAZER A FUNCAO DE REPARAR A DESTRUIDA
    
#     if new_solution.value < best_solution:
#         best_solution = new_solution
        
        
        
#     actualtime = time.time()-starttime
#     print(actualtime)


