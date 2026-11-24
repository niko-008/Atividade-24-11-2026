def listar_alunos(alunos):
    print("\n--- ALUNOS CADASTRADOS ---")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(
            f"Matrícula: {aluno['matricula']} | "
            f"Nome: {aluno['nome']} | "
            f"Idade: {aluno['idade']} | "
            f"Curso: {aluno['curso']}"
        )
