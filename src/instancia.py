# Programa resolução do Problema de Tabela Horario para Universidades na formatação cbctt proposta pelo ITC 2007 utilizando a meta-heuristica Large Neighborhood Search

from curriculo import *
from curso import *
from sala import *
    
class Instancia:
    def __init__(self):
        #print("init instancia")
        self.le_instancia()
    
    def le_instancia(self):
        self.leCabecalho()
        self.lista_cursos = self.leLista(Curso, Curso.leCurso, self.qtd_cursos)
        self.lista_salas = self.leLista(Sala, Sala.leSala, self.qtd_salas)
        self.lista_curriculos = self.leLista(Curriculo, Curriculo.leCurriculo, self.qtd_curriculos)
        self.leIndisponibilidades()
        
        #self.lista_indisponibilidades = self.leLista(Indisponibilidade, Indisponibilidade.leIndisponbilidade, self.qtd_indisponibilidades)
    
    def __str__(self):
        return self.str_Instancia()
    
    def str_Instancia(self):
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
        
        
        return string
    
    def str_Cabecalho(self):
        return f'Instancia {self.nome} \n{self.qtd_cursos} cursos, {self.qtd_salas} salas, {self.qtd_dias} dias, {self.qtd_horarios} periodos por dia, {self.qtd_curriculos} curriculos e {self.qtd_indisponibilidades} indisponibilidades'
        
    
    def leCabecalho(self):
        lixo, self.nome = input().split()
        qtd = input().split()
        self.qtd_cursos = int(qtd[1])
        qtd = input().split()
        self.qtd_salas = int(qtd[1])
        qtd = input().split()
        self.qtd_dias = int(qtd[1])
        qtd = input().split()
        self.qtd_horarios = int(qtd[1])
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
    
    
    def busca_curso_nome(self, nome):
        for i in range(self.qtd_cursos):
            if self.lista_cursos[i].nome == nome:
                return i
        return -1    
        
    
    def leIndisponibilidades(self):
        input()
        input()
        for i in range(self.qtd_indisponibilidades):
            curso, dia, horario = input().split()
            index = self.busca_curso_nome(curso)
            self.lista_cursos[index].insereIndisponibilidade(dia, horario)
            
            
            
            
            
            
            