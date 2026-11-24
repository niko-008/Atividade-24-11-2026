def excluir_aluno(alunos):
    print("\n--- EXCLUIR ALUNO ---")
    matricula = input("Digite a matrícula do aluno que deseja excluir: ").strip()

    for indice, aluno in enumerate(alunos):
        if aluno["matricula"] == matricula:
            confirmacao = input(
                f"Confirma a exclusão de {aluno['nome']}? (s/n): "
            ).strip().lower()

            if confirmacao == "s":
                alunos.pop(indice)
                print("Aluno excluído com sucesso.")
            else:
                print("Exclusão cancelada.")
            return

    print("Nenhum aluno encontrado com essa matrícula.")
