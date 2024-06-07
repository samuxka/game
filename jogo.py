import random
from personagem import escolher_classe, Personagem
from mecanica_defesa import defesa
from ataques import ataques

def criar_personagem():
    nome = input("Digite o nome do seu personagem: ")
    classe, vida_min, armadura_min, resistencia_magica_min, ataque_fisico_min, ataque_magico_min = escolher_classe()

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

def criar_personagem_jogador2():
    print("\nJogador 2, crie seu personagem.\n")
    return criar_personagem()

def determinar_quem_comeca(jogador1, jogador2):
    print("\nEscolha par ou ímpar:")
    print("1. Ímpar")
    print("2. Par")
    escolha = int(input("Digite o número da sua escolha: "))
    if escolha == 1:
        escolha_jogador1 = "ímpar"
        escolha_jogador2 = "par"
    elif escolha == 2:
        escolha_jogador1 = "par"
        escolha_jogador2 = "ímpar"
    else:
        print("Escolha inválida! Tente novamente.")
        return determinar_quem_comeca(jogador1, jogador2)

    resultado_dado_jogador1 = random.randint(1, 6)
    resultado_dado_jogador2 = random.randint(1, 6)
    
    print(f"{jogador1.nome} escolheu {escolha_jogador1}.")
    print(f"{jogador2.nome} escolheu {escolha_jogador2}.\n")

    total = resultado_dado_jogador1 + resultado_dado_jogador2
    print(f"Resultado do dado do {jogador1.nome}: {resultado_dado_jogador1}")
    print(f"Resultado do dado do {jogador2.nome}: {resultado_dado_jogador2}\n")

    print(f"Resultado {total}")
    if total % 2 == 0 and escolha == 1:
        print(f"{jogador1.nome} começa atacando!\n")
        return jogador1, jogador2
    elif total % 2 != 0 and escolha == 1:
        print(f"{jogador1.nome} começa atacando!\n")
        return jogador1, jogador2
    else:
        print(f"{jogador2.nome} começa atacando!\n")
        return jogador2, jogador1

def ataque(jogador_atacante, jogador_defensor):
    print(f"\n{jogador_atacante.nome}, é sua vez de atacar!")
    
    # Aqui você pode listar os ataques disponíveis para o jogador com base na classe
    print("Escolha seu ataque:")
    for i, ataque in enumerate(ataques[jogador_atacante.classe]):
        print(f"{i + 1}. {ataque['nome']}")
    
    escolha = int(input("Digite o número do ataque escolhido: "))

    # Verifica se a escolha do ataque é válida
    if escolha < 1 or escolha > len(ataques[jogador_atacante.classe]):
        print("Ataque inválido!")
        return

    ataque_escolhido = ataques[jogador_atacante.classe][escolha - 1]
    
    # Calcula se o ataque foi bem-sucedido com base na chance de sucesso
    if random.random() <= ataque_escolhido["chance"]:
        print(f"{jogador_atacante.nome} atacou com {ataque_escolhido['nome']}!")

        # Reduz a vida do jogador defensor com base no dano do ataque
        dano_causado = ataque_escolhido["dano"]
        jogador_defensor.vida -= dano_causado
        print(f"{jogador_defensor.nome} recebeu {dano_causado} de dano.")
    else:
        print(f"{jogador_atacante.nome} errou o ataque!")

    # Exibe o status atual dos jogadores após o ataque
    print("\nStatus atual dos jogadores:")
    exibir_status(jogador_atacante)
    exibir_status(jogador_defensor)

if __name__ == "__main__":
    print("Jogador 1, crie seu personagem.")
    jogador1 = criar_personagem()
    exibir_status(jogador1)

    jogador2 = criar_personagem_jogador2()
    exibir_status(jogador2)

    jogador_atacante, jogador_defensor = determinar_quem_comeca(jogador1, jogador2)
    
    while True:
        # Jogador atacante realiza o ataque
        ataque(jogador_atacante, jogador_defensor)

        if jogador_defensor.vida <= 0:
            print(f"\n{jogador_defensor.nome} foi derrotado! Parabéns, {jogador_atacante.nome}!")
            break

        # Jogador defensor escolhe sua defesa
        defesa(jogador_atacante, jogador_defensor)

        # Verifica se o jogador defensor ainda está vivo após a defesa
        if jogador_defensor.vida <= 0:
            print(f"\n{jogador_defensor.nome} foi derrotado! Parabéns, {jogador_atacante.nome}!")
            break

        # Troca os papéis dos jogadores (o defensor se torna o atacante e vice-versa)
        jogador_atacante, jogador_defensor = jogador_defensor, jogador_atacante
