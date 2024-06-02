import random

class Personagem:
    def __init__(self, nome, classe, vida, armadura, resistencia_magica, ataque_fisico, ataque_magico):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.armadura = armadura
        self.resistencia_magica = resistencia_magica
        self.ataque_fisico = ataque_fisico
        self.ataque_magico = ataque_magico

    def atacar_fisico(self, alvo, dano):
        # Cálculo do dano físico considerando a armadura do alvo
        dano_efetivo = max(0, dano - alvo.armadura * 0.4)
        alvo.vida -= dano_efetivo

    def atacar_magico(self, alvo, dano):
        # Cálculo do dano mágico considerando a resistência mágica do alvo
        dano_efetivo = max(0, dano - alvo.resistencia_magica * 0.35)
        alvo.vida -= dano_efetivo

# Ataques para cada classe
ataques = {
    "Tanque": [
        {"nome": "Investida do Touro", "dano": 160, "chance": 0.7},
        {"nome": "Soco do Camarão Mantis", "dano": 340, "chance": 0.4},
        {"nome": "Chicxulub", "dano": 760, "chance": 0.1}
    ],
    "Mago": [
        {"nome": "Explosão Arcana", "dano": 257, "chance": 0.7},
        {"nome": "Raio Ígneo", "dano": 381, "chance": 0.4},
        {"nome": "Chuva de Estrelas", "dano": 960, "chance": 0.1}
    ],
    "Lutador": [
        {"nome": "Martelo Trovejante", "dano": 198, "chance": 0.7},
        {"nome": "Investida Fulminante", "dano": 257, "chance": 0.4},
        {"nome": "Golpe Sísmico", "dano": 920, "chance": 0.1}
    ],
    "Assassino": [
        {"nome": "Lâmina Sombria", "dano": 360, "chance": 0.7},
        {"nome": "Veneno Sutil", "dano": 480, "chance": 0.4},
        {"nome": "Golpe Furtivo", "dano": 859, "chance": 0.1}
    ],
    "Atirador": [
        {"nome": "Disparo Preciso", "dano": 230, "chance": 0.7},
        {"nome": "Flecha Flamejante", "dano": 348, "chance": 0.4},
        {"nome": "Rajada Mortal", "dano": 985, "chance": 0.1}
    ]
}

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

def criar_personagem():
    nome = input("Digite o nome do seu personagem: ")
    classe, vida_min, armadura_min, resistencia_magica_min, ataque_fisico_min, ataque_magico_min = escolher_classe()
    
    # Para manter os atributos aleatórios mas acima dos mínimos, podemos adicionar um valor aleatório
    # Por exemplo, adicionando um valor entre 0 e 100 a cada atributo mínimo
    vida = vida_min + random.randint(0, 100)
    armadura = armadura_min + random.randint(0, 20)
    resistencia_magica = resistencia_magica_min + random.randint(0, 20)
    ataque_fisico = ataque_fisico_min + random.randint(0, 50)
    ataque_magico = ataque_magico_min + random.randint(0, 50)
    
    return Personagem(nome, classe, vida, armadura, resistencia_magica, ataque_fisico, ataque_magico)

def exibir_status(personagem):
    print(f"\nNome: {personagem.nome}")
    print(f"Classe: {personagem.classe}")
    print(f"Vida: {personagem.vida}")
    print(f"Armadura: {personagem.armadura}")
    print(f"Resistência Mágica: {personagem.resistencia_magica}")
    print(f"Ataque Físico: {personagem.ataque_fisico}")
    print(f"Ataque Mágico: {personagem.ataque_magico}")

def par_ou_impar():
    print("Escolha par ou ímpar:")
    print("1. Ímpar")
    print("2. Par")
    escolha = int(input("Digite o número da escolha: "))
    if escolha == 1:
        return "ímpar"
    elif escolha == 2:
        return "par"
    else:
        print("Escolha inválida!")
        return par_ou_impar()

def determinar_quem_comeca(jogador1, jogador2):
    escolha = par_ou_impar()
    print(f"\n{jogador1.nome} escolheu {escolha}.")
    print("\nRolando o dado para escolher quem começa atacando...")
   
