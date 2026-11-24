def cadastrar_aluno(alunos):
    print("\n--- CADASTRAR ALUNO ---")
    nome = input("Nome: ").strip()

    if not nome:
        print("O nome não pode ficar vazio.")
        return

    matricula = input("Matrícula: ").strip()

    if not matricula:
        print("A matrícula não pode ficar vazia.")
        return

    if any(aluno["matricula"] == matricula for aluno in alunos):
        print("Já existe um aluno com essa matrícula.")
        return

    idade_texto = input("Idade: ").strip()
    if not idade_texto.isdigit() or int(idade_texto) <= 0:
        print("Informe uma idade válida.")
        return

    curso = input("Curso: ").strip()
    if not curso:
        print("O curso não pode ficar vazio.")
        return

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "idade": int(idade_texto),
        "curso": curso
    }

    alunos.append(aluno)
    print(f"Aluno(a) {nome} cadastrado(a) com sucesso!")
