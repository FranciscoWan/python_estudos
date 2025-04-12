print(50*"-")
login_sistema = input(f"{6*" "}Defina seu nome de login: ")
senha_sistema = input(f"{6*" "}Defina uma senha para o sistema: ")


qtd_tentativas = 3
login_usuario = ""
senha_usuario = ""

while True:
    print(50*"-")
    login_usuario = input(f"{10*" "}Login: ")
    senha_usuario = input(f"{10*" "}Senha: ")
    print(50*"-")
    qtd_tentativas -= 1
    if login_sistema != login_usuario and senha_sistema != senha_usuario and qtd_tentativas != 0:
        print("Login e senha estão incorretos")
    elif login_sistema == login_usuario and senha_sistema != senha_usuario and qtd_tentativas != 0:
        print("Senha incorreta!")
    elif login_sistema == login_usuario and senha_sistema == senha_usuario:
        print(f"{10*" "}Acesso concedido!")
        break
    if qtd_tentativas == 0:
        print(f"{6*" "}Suas tentativas acabaram.\n{6*" "}Acesso BLOQUEADO!")
        break
    print(f"Você ainda possui {qtd_tentativas} chances para acessar o sistema.")