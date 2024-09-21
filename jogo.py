class Personagem():
    def __init__(self,nome,nivel,vida):
        self.__nome = nome
        self.__nivel = nivel
        self.__vida = vida

    def get_nome(self):
        return self.__nome

    def get_nivel(self):
        return self.__nivel

    def get_vida(self):
        return self.__nivel
    
class Heroi(Personagem):
    def __init__(self, nome, nivel, vida, habilidade):
        super().__init__(nome, nivel, vida)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade