import random

def defesa(jogador_atacante, jogador_defensor):
    print(f"\n{jogador_defensor.nome}, é sua vez de se defender!")

    # Opções de defesa disponíveis para o jogador
    print("Escolha sua defesa:")
    print("1. Bloquear")
    print("2. Esquivar")
    print("3. Contra-atacar")
    escolha = int(input("Digite o número da sua escolha: "))

    # Dicionário de opções de defesa e suas características (chance de sucesso)
    opcoes_defesa = {
        1: {"nome": "Bloquear", "chance": 0.85},  # Exemplo de opção de defesa
        2: {"nome": "Esquivar", "chance": 0.7},   # Exemplo de opção de defesa
        3: {"nome": "Contra-atacar", "chance": 0.5}  # Exemplo de opção de defesa
    }

    # Verifica se a escolha de defesa é válida
    if escolha not in opcoes_defesa:
        print("Opção de defesa inválida! Você não se defendeu.")
        return

    opcao_escolhida = opcoes_defesa[escolha]

    # Calcula se a defesa foi bem-sucedida com base na chance de sucesso
    if random.random() <= opcao_escolhida["chance"]:
        print(f"{jogador_defensor.nome} escolheu {opcao_escolhida['nome']} e se defendeu com sucesso!")
        # Reduz ou evita o dano recebido, dependendo da opção de defesa escolhida
        # Aqui você pode adicionar lógica para reduzir o dano recebido
    else:
        print(f"{jogador_defensor.nome} escolheu {opcao_escolhida['nome']} mas falhou na defesa.")
