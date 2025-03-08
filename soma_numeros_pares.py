inicio = int(input("Qual o início do intervalo que deseja somar: "))
fim = int(input("Qual o final do intervalo que deseja somar: "))
soma = 0

for i in range(inicio, fim):
    if i%2 == 0:
        soma += i
    else:
        soma += 0
if soma == 0:
    print(f"Só existem números ímpares no intervalor de {inicio} a {fim}")

print(f"A soma dos números pares do intervalo de {inicio} a {fim} foi de: {soma}.")