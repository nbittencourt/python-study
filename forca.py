def jogar():
    print(20*"*")
    print("Bem vindo ao jogo de Forca!")
    print(20*"*")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    
    while (not enforcou and not acertou):
        print(f"Essa é a palavra secreta: {letras_acertadas}")
        chute = input("Escolha uma letra: ").lower().strip()

        index = 0
        result = ""
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra

            index = index + 1

    print(f"Essa é a palavra secreta: {palavra_secreta} e você churou {letras_acertadas}")
    print("Fim de jogo...")

if (__name__ == "__main__"):
    jogar()