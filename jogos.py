import adivinhacao
import forca

print(20*"*")
print("Menu de Jogos")
print(20*"*")

print("(1) Forca; (2) Adivinhação")
jogo = int(input("Qual jogo você quer?"))

if (jogo == 1) :
    print("Jogando Forca...")
    forca.jogar()
elif (jogo == 2):
    print("Jogando Adivinhação...")
    adivinhacao.jogar()
else:
    print("Não conheço esse jogo...")