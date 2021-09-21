import random

def jogar():
    print(20*"*")
    print("Bem vindo ao jogo de Adivinhação!")
    print(20*"*")

    numero_secreto =random.randrange(1, 101) # de 1 a 100
    pontos = 100

    print("Qual nível de dificuldade desejado?")
    print("1 - Fácil, 2 - Médio, 3 - Difícil")
    nivel_str = input("Nível: ")
    nivel = int(nivel_str)

    total_tentativas = 5 * (4 - nivel)
    pontos = pontos * nivel


    for rodada in range (1, total_tentativas + 1):
        print(f"Tentativa {rodada} de {total_tentativas}")
        chute_str = input("Digite um numero de 1 a 100: ")
        print("Você digitou {}".format(chute_str))
        chute = int(chute_str)

        if ((chute < 1) or (chute > 100)):
            print("Você deve escolher um numero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"ACERTOU! Você fez {pontos} pontos!")
            break
        elif (maior):
            print("Você chutou pra cima!")
        elif (menor):
            print("Você chutou pra baixo!")
        pontos = pontos - abs(chute - numero_secreto)
        
    print(f"Acabou... O número secreto era {numero_secreto}.")

if (__name__ == "__main__"):
    jogar()