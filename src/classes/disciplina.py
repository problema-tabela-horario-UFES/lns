#Incompleto

class Disciplina:
    def __init__(self, nome=""):
        self.nome = nome
        
    def __str__(self):
        return f'Disciplina'
    
    def leDisciplina(self):
        disciplina = input()