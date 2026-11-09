alunos = {}

while True:

    R=input("1- Inseir\n2- Listar\n3- Sair\nR:")

    if R == "1":
        print("Inserir aluno:")
        nome=input("Nome: ")
        idade=int(input("Idade: "))
        curso=input("Curso: ")
        alunos[nome] = {"idade":idade, "curso":curso}
    elif R == "2":
        print("Listar alunos:")
        for nome_aluno, dados in alunos.items():
                print(f"\nNome: {nome_aluno}")
                print(f"Idade: {dados['idade']}")
                print(f"Curso: {dados['curso']}")
    elif R == "3":
        break
    else:
        print("Erro")

