import random
import time

def jogo_numeros_aleatorios():
    restart = "sim"
    while restart.lower() == "sim":
            numero_aleatorio = random.randint(1, 100)
            palpite = -1
            count = 0
            print("\nEstou pensando em um número de 1 a 100. Tente adivinhar.")
            time.sleep(1)
            while palpite != numero_aleatorio:
                
                palpite = int(input("\nQual seu palpite: "))
                count += 1
                if palpite > numero_aleatorio:
                    print("Você chutou um número muito alto.")
                    print("O número que pensei é mais baixo.")
                    time.sleep(1)
                elif palpite < numero_aleatorio:
                    print("Você chutou um número muito baixo.")
                    print("O número que pensei é mais alto.")
                    time.sleep(1)
                else:
                    print(f"Você precisou de {count} palpites para adivinhar meu número! Parabéns você ganhouuu!!!\n\n")
                    time.sleep(1)
                    restart = str(input("Você quer jogar de novo? \n 'sim' \n 'não' \n  "))
    print("\nJogo Encerrado!\n")
                

jogo_numeros_aleatorios()