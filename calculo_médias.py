def calcular_media_alunos():

    n_notas = int(input("Digite o número de alunos que irá calcular as notas: "))

    for i in range(n_notas):
        nome_aluno = str(input("Nome do aluno: "))
        media = 0
        nota_total = 0
        lista_nota = []
        for _ in range(1, 4):
            nota = float(input(f"Digite a {_}º nota: "))
            lista_nota.append(nota)
            nota_total += nota
            media = nota_total/3
            
        print(f'''\n    Aluno: {nome_aluno}
        Nota 1: {lista_nota[0]}
        Nota 2: {lista_nota[1]}
        Nota 3: {lista_nota[2]}
        Média: {media:.1f}''')

        if media >= 7:
            print("    Situação: ## APROVADO ##\n")
        elif media < 7:
            print("    Situação: ## REPROVADO ##\n")

calcular_media_alunos()