import random

def escolher_classe():
    print("Escolha uma classe:")
    print("1. Tanque")
    print("2. Mago")
    print("3. Lutador")
    print("4. Assassino")
    print("5. Atirador")
    
    escolha = int(input("Digite o número da classe escolhida: "))
    
    if escolha == 1:
        return "Tanque", 3000, 320, 240, 120, 0
    elif escolha == 2:
        return "Mago", 1512, 60, 40, 0, 840
    elif escolha == 3:
        return "Lutador", 1302, 70, 256, 850, 312
    elif escolha == 4:
        return "Assassino", 1620, 70, 23, 220, 540
    elif escolha == 5:
        return "Atirador", 1200, 40, 30, 920, 140
    else:
        print("Escolha inválida!")
        return escolher_classe()

class Personagem:
    def __init__(self, nome, classe, vida, armadura, resistencia_magica, ataque_fisico, ataque_magico):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.armadura = armadura
        self.resistencia_magica = resistencia_magica
        self.ataque_fisico = ataque_fisico
        self.ataque_magico = ataque_magico