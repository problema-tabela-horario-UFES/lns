# Faz a leitura inicial do programa 

class Cabecalho:
    def __init__(self, nome="", qtd_cursos="", qtd_salas="", qtd_dias="", periodos_por_dia="", qtd_curriculos="", qtd_indisponibilidades=""):
        self.nome = nome
        self.qtd_cursos = qtd_cursos
        self.qtd_salas = qtd_salas
        self.qtd_dias = qtd_dias
        self.periodos_por_dia = periodos_por_dia
        self.qtd_curriculos = qtd_curriculos
        self.qtd_indisponibilidades = qtd_indisponibilidades
        
    def __str__(self):
        return f'Instancia {self.nome} \n{self.qtd_cursos} cursos, {self.qtd_salas} salas, {self.qtd_dias} dias, {self.periodos_por_dia} periodos por dia, {self.qtd_curriculos} curriculos e {self.qtd_indisponibilidades} indisponibilidades'
        
        
    def leCabecalho(self):
        lixo, self.nome = input().split()
        lixo, self.qtd_cursos = input().split()
        lixo, self.qtd_salas = input().split()
        lixo, self.qtd_dias = input().split()
        lixo, self.periodos_por_dia = input().split()
        lixo, self.qtd_curriculos = input().split()
        lixo, self.qtd_indisponibilidades = input().split()
