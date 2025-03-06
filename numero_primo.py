#Calcular se um número é primo

numero = int(input("Digite um número para descobrir se é primo: "))
final = numero+1
divisao = 0
for i in range(1, final):
    if numero%i == 0:
        divisao += 1
if divisao == 2:
    print("O número é PRIMO")
else:
    print("O número NÃO É PRIMO")
    
