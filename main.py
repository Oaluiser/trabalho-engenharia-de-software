import random

# caminho = "/Users/oaluiser/Documents/GitHub/senac-analise-e-desenvolvimento-de-sistemas/Terceiro Semestre/Algoritmos e Estrutura de Dados/trabalho1/"

# Felipe Radmann - reaproveitando variavel!

caminho = "C:/Users/TIBUFF/trabalho-engenharia-de-software/"
pontuacao = 0

# Rodrigo Gastaud - Cria uma função apenas para converter os dados dos arquivos em listas, seguindo os principios de clean code, onde uma função deve ter um único propósito e executá-lo bem.
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
                
# Dieizon Oliveira - Cria uma função exibeAlternativas para ser chamada logo abaixo, substituindo o for existente anteriormente, seguindo os principios de clean code, tornando o código mais legivel e de mais fácil entendimento.
def exibeAlternativas(alternativas, numero):
    for i in range(0, 4):
        print(alternativas[numero][i])

def iniciaJogo():
    global pontuacao
    if pontuacao < 4:
        arquivo = open(
            caminho + "facil.txt",
            "r",
        )
    elif pontuacao < 8:
        arquivo = open(
            caminho + "medio.txt",
            "r",
        )
    else:
        arquivo = open(
            caminho + "dificil.txt",
            "r",
        )

    perguntas = arquivo.readlines()
    arquivo.close()

    arrayPerguntas = []
    arrayRespostas = []
    arrayAlternativas = []

    converteParaPergunta(arrayPerguntas,arrayRespostas,arrayAlternativas, perguntas)

    numero = random.randint(0, 7)
    print(arrayPerguntas[numero])
    exibeAlternativas(arrayAlternativas, numero)
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
            caminho + "ranking.txt",
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
            caminho + "ranking.txt",
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