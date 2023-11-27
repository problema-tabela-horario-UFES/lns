# Programa resolução do Problema de Tabela Horario para Universidades na formatação cbctt proposta pelo ITC 2007 utilizando a meta-heuristica Large Neighborhood Search

from solucao import *
from instancia import *


DEBUG = False
DEBUG_CUSTO = False
timelimit = 180

import sys

for i, arg in enumerate(sys.argv):
    #print(i, arg)
    if "timelimit=" in arg:
        timelimit = int(arg.strip("timelimit="))
        
#print("time limit", timelimit)


s = Solucao()
#print("Inicial", s.solucao_inicial)

sol = s.lns(timelimit)
#print(sol)
print(s.str_Solucao(sol), "\nCusto:", s.calculaCusto(sol))
