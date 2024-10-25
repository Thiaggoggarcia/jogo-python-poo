from random import randint

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
    
    def atacar(self, alvo):
        dano = randint(self.__nivel * 2, self.__nivel*4)
        alvo.receber_dano(dano)
        print(f"\n{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
        
    def receber_dano(self,dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
        
        
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade_especial):
        super().__init__(nome, vida, nivel)
        self.__habilidade_especial = habilidade_especial
        
    def ataque_especial(self, alvo):
        dano = randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_dano(dano)
        print(f"\n{self.get_nome()} usou a habilidade especial de {self.get_habilidade_especial()} em  {alvo.get_nome()} e causou {dano} de dano!")
   
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade Especial: {self.__habilidade_especial}"
    
    def get_habilidade_especial(self):
        return self.__habilidade_especial


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.__tipo}"
    
    
class Jogo:
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Thiago", vida=100, nivel= 5, habilidade_especial="Super Velocidade")
        self.inimigo = Inimigo(nome="Dragão", vida=100, nivel=6, tipo="Voador")
    
    def iniciar_batalha(self):
        print("Iniciando Batalha....\n")
        
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("***** Dados dos Personagens *****")
            print(self.heroi.exibir_detalhes())
            print()
            print(self.inimigo.exibir_detalhes())
            
            input("\nPressione Enter para Atacar....")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial): ")      

            if escolha == "1":
                self.heroi.atacar(self.inimigo)

            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            
            else:
                print("Opção inválida, tente novamente!")
                
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        if self.inimigo.get_vida() == 0:
            print(f"{self.heroi.get_nome()} venceu a batalha!")
        
        else:
            print(f"{self.inimigo.get_nome()} venceu a batalha!")
    
jogo = Jogo()
jogo.iniciar_batalha()