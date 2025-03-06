import time

def cronometro():
    input("\n⏳ Pressione ENTER para iniciar o cronômetro...\n")
    inicio = time.time() 

    input("Pressione ENTER novamente para parar.")
    fim = time.time()  

    tempo_decorrido = fim - inicio
    print(f"\n⏰ Tempo decorrido: {tempo_decorrido:.2f} segundos\n")

cronometro()
