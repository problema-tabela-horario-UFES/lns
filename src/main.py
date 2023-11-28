# Programa resolução do Problema de Tabela Horario para Universidades na formatação cbctt proposta pelo ITC 2007 utilizando a meta-heuristica Large Neighborhood Search

from solucao import *
from instancia import *

timelimit = 180
g = False
d = False
dc = False
import sys

for i, arg in enumerate(sys.argv):
    #print(i, arg)
    if "--timelimit=" in arg:
        #print(arg.strip("timelimit="))
        timelimit = int(arg.strip("--timelimit="))
    if "--grafico" in arg:
        g = True
    if "--debug" in arg:
        d = True
        
#print("time limit", timelimit)


s = Solucao(GRAFICO=g, DEBUG=d, DEBUG_CUSTO=dc)
#print("Inicial", s.solucao_inicial)

sol = s.lns(timelimit)
#print(sol)

print(s.str_Solucao(sol), "\nCusto e Iteracoes:", s.calculaCusto(sol), s.ite)
