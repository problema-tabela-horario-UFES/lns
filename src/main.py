# Programa resolução do Problema de Tabela Horario para Universidades na formatação cbctt proposta pelo ITC 2007 utilizando a meta-heuristica Large Neighborhood Search

from solucao import *
from instancia import *

timelimit = 60

s = Solucao()
#print("Inicial", s.solucao_inicial)

sol = s.lns(timelimit)
#print(sol)
print(s.str_Solucao(sol), "\nCusto:", s.calculaCusto(sol))