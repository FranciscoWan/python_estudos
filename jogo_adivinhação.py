import random
import time

numero_aleatorio = random.randint(1, 10)

tentativas = 3
while tentativas >= 1:
    print(f"Estou pensando em um número aleatório de 1 a 10. Você tem {tentativas} tentativas para adivinhar.\n")
    palpite = int(input("Qual seu palpite: "))
    tentativas -= 1
    time.sleep(1)
    if numero_aleatorio == palpite:
        print(f"Eu pensei no número {numero_aleatorio} e você deu o palpite de {palpite}.")
        print("Parabéns!!! Você acertou!!!")
        break
    elif numero_aleatorio != palpite:
        print(f"\nEu não pensei no número {palpite}.")
        if tentativas == 0:
            print("Você não conseguiu acertar em três tentativas. Você perdeu!")       
