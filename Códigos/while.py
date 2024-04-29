numero_secreto = 23
palpite = None

while palpite != numero_secreto:
    palpite = int(input("Digite um número: "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
    else:
        if palpite > numero_secreto:
            print("O número secreto é menor!")
        else:
            print("O número secreto é maior!")
