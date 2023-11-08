class Curriculo:
    def __init__(self, nome="", qtd_disciplinas=0, lista_disciplinas=[]):
        self.nome = nome
        self.qtd_disciplinas = qtd_disciplinas
        self.lista_disciplinas = lista_disciplinas

    def __str__(self):
        return f'Curriculo {self.nome} ({self.qtd_disciplinas}), disciplinas: {self.lista_disciplinas}'
        
    def leCurriculo(self):
        curriculo = input().split()
        self.nome = curriculo[0]
        self.qtd_disciplinas = int(curriculo[1])
        self.lista_disciplinas = []
        for i in range(self.qtd_disciplinas):
            self.lista_disciplinas.append(curriculo[i+2])
        