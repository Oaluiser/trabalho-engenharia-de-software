import random

pontuacao = 0

# Rodrigo Gastaud - Cria uma função apenas para converter os dados dos arquivos em listas, seguindo os princípios de clean code, onde uma função deve ter um único propósito e executá-lo bem.
def converteParaPergunta(listaPerguntas, listaRespostas, listaAlternativas, arquivo):
    for i in range(0, 8):
        for j in range(0, 3):
            if j == 0:
                listaPerguntas.append(arquivo[i * 7 + j])
            if j == 1:
                listaRespostas.append(arquivo[i * 7 + j])
            if j == 2:
                alternativas = []
                for k in range(0, 4):
                    alternativas.append(arquivo[i * 7 + j + k])
                listaAlternativas.append(alternativas)
                
# Dieizon Oliveira - Cria uma função exibeAlternativas para ser chamada logo abaixo, substituindo o for existente anteriormente, seguindo os princípios de clean code, tornando o código mais legível e de mais fácil entendimento.
def exibeAlternativas(alternativas, numero):
    for i in range(0, 4):
        print(alternativas[numero][i])

# Felipe Radmann - Cria uma função para exibir uma pergunta aleatória e suas alternativas, seguindo os principios do clean code.
def exibePerguntaAleatoria(perguntas, alternativas):
    numero = random.randint(0, len(perguntas) - 1)
    print(perguntas[numero])
    exibeAlternativas(alternativas, numero)
    return numero

# Felipe Radmann - Cria uma funçao, para pedir ao usuario uma uma resposta.
def recebeResposta():
    return input("Digite a resposta: ")

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
            "/Users/oaluiser/Documents/GitHub/senac-analise-e-desenvolvimento-de-sistemas/Terceiro Semestre/Algoritmos e Estrutura de Dados/trabalho1/dificil.txt",
            "r",
        )

    perguntas = arquivo.readlines()
    arquivo.close()

    arrayPerguntas = []
    arrayRespostas = []
    arrayAlternativas = []

    converteParaPergunta(arrayPerguntas, arrayRespostas, arrayAlternativas, perguntas)

    #Felipe Radmann - Pegando os valores das funçoes para validaçoes.
    numero_pergunta = exibePerguntaAleatoria(arrayPerguntas, arrayAlternativas)
    resposta = recebeResposta()

    if resposta == arrayRespostas[numero_pergunta][-2]:
        print("Resposta correta")
        pontuacao += 1
        iniciaJogo()
    else:
        print("Resposta errada")
        print("A resposta correta era: ", arrayRespostas[numero_pergunta])
        print("Sua pontuação foi: ", pontuacao)
        nome = input("Digite seu nome:")

        caminho_ranking = "/Users/oaluiser/Documents/GitHub/senac-analise-e-desenvolvimento-de-sistemas/Terceiro Semestre/Algoritmos e Estrutura de Dados/trabalho1/ranking.txt"
        with open(caminho_ranking, "a") as arquivo_ranking:
            arquivo_ranking.write(nome + " " + str(pontuacao) + "\n")

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
        caminho_ranking = "/Users/oaluiser/Documents/GitHub/senac-analise-e-desenvolvimento-de-sistemas/Terceiro Semestre/Algoritmos e Estrutura de Dados/trabalho1/ranking.txt"
        with open(caminho_ranking, "r") as arquivo:
            ranking = arquivo.readlines()
            ranking.sort(key=lambda x: int(x.split()[1]), reverse=True)
            for line in ranking:
                print(line.strip())
    elif opcao == "3":
        break
    else:
        print("Opção inválida")
