class Curso:
    def __init__(self, nome="", professor="", qtd_aulas=0, num_min_dias=0, qtd_alunos=0):
        self.nome = nome
        self.professor = professor 
        self.qtd_aulas = qtd_aulas
        self.num_min_dias = num_min_dias 
        self.qtd_alunos = qtd_alunos
        self.qtd_indisponibilidades = 0
        self.lista_indisponibilidades = []
        
    def __str__(self):
        string = f'Curso {self.nome} ({self.qtd_alunos}), Professor {self.professor}, {self.qtd_aulas} aulas em pelo menos {self.num_min_dias} dias\n'
        string += 'Indisponivel: '
        for i in self.lista_indisponibilidades:
            string += f'{i} '
        return string
    
    def leCurso(self):
        self.nome, self.professor, qtd_aulas, num_min_dias, qtd_alunos = input().split()
        self.qtd_alunos = int(qtd_alunos)
        self.num_min_dias = int(num_min_dias)
        self.qtd_aulas = int(qtd_aulas)
        
    def insereIndisponibilidade(self, dia, horario):
        indisponibilidade = [dia, horario]
        self.lista_indisponibilidades.append(indisponibilidade)
        self.qtd_indisponibilidades += 1