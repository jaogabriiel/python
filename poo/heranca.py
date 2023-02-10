class NPC: # base, pai, super
    def __init__(self, nome, time, forca, municao):
        self. nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True # valor fixo não precisa ser passado com parâmetro
        self.energia = 100 # valor fixo não precisa ser passado com parâmetro
        
        
    def info(self):
        print(f'Nome: \t{self.nome}')
        print(f'Time: \t{self.time}')
        print(f'Força: \t{self.forca}')
        print(f'Munição: \t{self.municao}')
        print(f'Vivo: \t{"Sim" if self.vivo else "Não"}')
        print(f'Energia: \t{self.energia}')
        print('-'*30)
        
        
class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)
        

class guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)
        
        
class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)
        