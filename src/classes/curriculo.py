class Curriculo:
    def __init__(self, nome="", qtd_disciplinas=0, lista_disciplinas=[]):
        self.nome = nome
        self.qtd_disciplinas = qtd_disciplinas
        self.lista_disciplinas = lista_disciplinas

    def __str__(self):
        return f'Curriculo {self.nome} ({self.qtd_disciplinas}), disciplinas: {self.lista_disciplinas}\n'
        
    # def leCurriculo(self):
    #     # TO DO
    #     # TERMINAR DE FAZER A LEITURA DE CURRICULO
    #     # VER SOBRE COMO ITERAR SOBRE O INPUT
    #     curriculo = [] 
    #     curriculo = input().split()
    #     self.nome = curriculo[0]
    #     self.qtd_disciplinas = curriculo[1]
    #     self.lista_disciplinas = resto
    #     self.nome, self.qtd_disciplinas, list = input()
        