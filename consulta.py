def consultar_aluno(alunos):
    print("\n--- CONSULTAR ALUNO ---")
    matricula = input("Digite a matrícula do aluno: ").strip()

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print("\nAluno encontrado:")
            print(f"Nome: {aluno['nome']}")
            print(f"Matrícula: {aluno['matricula']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Curso: {aluno['curso']}")
            return

    print("Nenhum aluno encontrado com essa matrícula.")
