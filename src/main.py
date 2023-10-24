# Programa resolução do Problema de Tabela Horario para Universidades na formatação cbctt proposta pelo ITC 2007 utilizando a meta-heuristica Large Neighborhood Search

from classes.cabecalho import *
from classes.curriculo import *
from classes.disciplina import *
from classes.indisponibilidade import *
from classes.sala import *



def readInput():
    print("OK")    
    
def testReadInput():
    print("Teste Cabecalho:\n")

    cab = Cabecalho() ; cab.leCabecalho()
    print(cab)


    # SE BASEAR NISSO AQUI PARA FAZER A LEITURA DOS DADOS
    list_cur = []
    for i in range(cab.qtd_curriculos):
        cur = Curriculo() ; #cur.leCurriculo()
        print(cur)
        list_cur.append(cur)



    # DAQUI PARA BAIXO TUDO ERRADO
    
    
    dis = Disciplina() ; #dis.leDisciplina()
    print(dis)
    
    sal = Sala() ; sal.leSala()
    print(sal)
    
    ind = Indisponibilidade() ; #ind.leIndisponbilidade()
    print(ind)
    
    



    print("Fim Programa\n")


testReadInput()