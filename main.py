import random

pontuacao = 0


# Aluisio Pereira - Renomeia a função sorteiaPergunta para iniciaJogo, seguindo os principios de clean code, onde o nome da função deve ser um verbo que descreva o que a função faz.
def iniciaJogo():
    global pontuacao
    if pontuacao < 4:
        arquivo = open(
            "/Users/oaluiser/Documents/GitHub/senac-analise-e-desenvolvimento-de-sistemas/Terceiro Semestre/Algoritmos e Estrutura de Dados/trabalho1/facil.txt",
            "r",
        )
    elif pontuacao < 8:
        arquivo = open(
            "/Users/oaluiser/Documents/GitHub/senac-analise-e-desenvolvimento-de-sistemas/Terceiro Semestre/Algoritmos e Estrutura de Dados/trabalho1/medio.txt",
            "r",
        )
    else:
        arquivo = open(
            "/Users/oaluiser/Documents/GitHub/senac-analise-e-desenvolvimento-de-sistemas/Terceiro Semestre/Algoritmos e Estrutura de Dados/trabalho1/.txt",
            "r",
        )

    perguntas = arquivo.readlines()
    arquivo.close()

    arrayPerguntas = []
    arrayRespostas = []
    arrayAlternativas = []

    for i in range(0, 8):
        for j in range(0, 3):
            if j == 0:
                arrayPerguntas.append(perguntas[i * 7 + j])
            if j == 1:
                arrayRespostas.append(perguntas[i * 7 + j])
            if j == 2:
                alternativas = []
                for k in range(0, 4):
                    alternativas.append(perguntas[i * 7 + j + k])
                arrayAlternativas.append(alternativas)

    numero = random.randint(0, 7)
    print(arrayPerguntas[numero])
    for i in range(0, 4):
        print(arrayAlternativas[numero][i])
    resposta = input("Digite a resposta: ")

    if resposta == arrayRespostas[numero][-2]:
        print("Resposta correta")
        pontuacao += 1
        iniciaJogo()
    else:
        print("Resposta errada")
        print("A resposta correta era: ", arrayRespostas[numero])
        print("Sua pontuação foi: ", pontuacao)
        nome = input("Digite seu nome:")
        open(
            "/Users/oaluiser/Documents/GitHub/senac-analise-e-desenvolvimento-de-sistemas/Terceiro Semestre/Algoritmos e Estrutura de Dados/trabalho1/ranking.txt",
            "a",
        ).write(nome + " " + str(pontuacao) + "\n")
        pontuacao = 0


while True:
    print("Bem-vindo ao Quiz da Bola")
    print("1 - Jogar")
    print("2 - Ranking")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        iniciaJogo()
    elif opcao == "2":
        print("Ranking:")
        arquivo = open(
            "/Users/oaluiser/Documents/GitHub/senac-analise-e-desenvolvimento-de-sistemas/Terceiro Semestre/Algoritmos e Estrutura de Dados/trabalho1/ranking.txt",
            "r",
        )
        ranking = arquivo.readlines()
        arquivo.close()
        ranking.sort(key=lambda x: int(x.split()[1]), reverse=True)
        for i in range(0, len(ranking)):
            print(ranking[i])
    elif opcao == "3":
        break
    else:
        print("Opção inválida")
