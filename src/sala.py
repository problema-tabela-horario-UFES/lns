class Sala:
    def __init__(self, nome="", capacidade=0):
        self.nome = nome
        self.capacidade = int(capacidade)
              
    def __str__(self):
        return f'Sala {self.nome} ({self.capacidade})'
    
    def leSala(self):
        self.nome, self.capacidade = input().split()