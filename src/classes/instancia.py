# Programa resolução do Problema de Tabela Horario para Universidades na formatação cbctt proposta pelo ITC 2007 utilizando a meta-heuristica Large Neighborhood Search

from .curriculo import *
from .curso import *
from .indisponibilidade import *
from .sala import *
    
class Instancia:
    def __init__(self):
        self.leCabecalho()
        self.lista_cursos = self.leLista(Curso, Curso.leCurso, self.qtd_cursos)
        self.lista_salas = self.leLista(Sala, Sala.leSala, self.qtd_salas)
        self.lista_curriculos = self.leLista(Curriculo, Curriculo.leCurriculo, self.qtd_curriculos)
        self.lista_indisponibilidades = self.leLista(Indisponibilidade, Indisponibilidade.leIndisponbilidade, self.qtd_indisponibilidades)
            
    def __str__(self):
        string = self.str_Cabecalho()
        
        string += "\nCursos:\n"
        for i in range(self.qtd_cursos):
            string += str(self.lista_cursos[i]) + "\n"
            
        string += "\nSalas:\n"
        for i in range(self.qtd_salas):
            string += str(self.lista_salas[i]) + "\n"
            
        string += "\nCurriculos\n"
        for i in range(self.qtd_curriculos):
            string += str(self.lista_curriculos[i]) + "\n"
            
        string += "\nIndisponibilidades\n"
        for i in range(self.qtd_indisponibilidades):
            string += str(self.lista_indisponibilidades[i]) + "\n"
        
        
        return string
    
    def str_Cabecalho(self):
        return f'Instancia {self.nome} \n{self.qtd_cursos} cursos, {self.qtd_salas} salas, {self.qtd_dias} dias, {self.qtd_periodos_por_dia} periodos por dia, {self.qtd_curriculos} curriculos e {self.qtd_indisponibilidades} indisponibilidades'
        
    
    def leCabecalho(self):
        lixo, self.nome = input().split()
        qtd = input().split()
        self.qtd_cursos = int(qtd[1])
        qtd = input().split()
        self.qtd_salas = int(qtd[1])
        qtd = input().split()
        self.qtd_dias = int(qtd[1])
        qtd = input().split()
        self.qtd_periodos_por_dia = int(qtd[1])
        qtd = input().split()
        self.qtd_curriculos = int(qtd[1])
        qtd = input().split()
        self.qtd_indisponibilidades = int(qtd[1])
    
    def leLista(self, class_name, read_func, qtd):
        lista = []
        input()
        input()
        for i in range(qtd):
            c = class_name()
            read_func(c)
            #print(c)
            lista.append(c)
            
        return lista