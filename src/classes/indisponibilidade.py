class Indisponibilidade:
    def __init__(self, curso="", dia=None, horario=None):
        self.curso = curso
        self.dia = dia
        self.horario = horario
        
    def __str__(self):
        return f'Curso {self.curso} indisponivel dia {self.dia} horário {self.horario}'
    
           
    def leIndisponbilidade(self):
        self.curso, self.dia, self.horario = input().split()