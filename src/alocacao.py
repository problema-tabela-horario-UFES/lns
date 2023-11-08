# proposta inicial para alocacao de uma disciplina
# talvez seja alterado para uso de uma matriz

class Alocacao:
    def __init__(self, str_disciplina, str_sala, dia, horario):
        self.disciplina = str_disciplina
        self.sala = str_sala
        self.dia = dia
        self.horario = horario
    
    def __str__(self):
        return f'Aloc'
    
    