class Personagem:
    def __init__(self, nome,vida,nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
        
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade_especial):
        super().__init__(nome, nivel, vida)
        self.__habilidade_especial = habilidade_especial
        
    def get_habilidade_especial(self):
        return self.__habilidade_especial
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade Especial: {self.__habilidade_especial}"


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.__tipo}"
    
    
    
heroi = Heroi("Thiago", 100, 5, "Força")
print(heroi.exibir_detalhes())
print()
inimigo = Inimigo("Zezim", 85, 5, "Voador")

print(inimigo.exibir_detalhes())