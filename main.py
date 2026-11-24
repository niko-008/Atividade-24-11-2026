from cadastro import cadastrar_aluno
from listagem import listar_alunos
from consulta import consultar_aluno
from exclusao import excluir_aluno


def menu():
    alunos = []

    while True:
        print("\n===== SISTEMA DE CADASTRO DE ALUNOS =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Consultar aluno")
        print("4 - Excluir aluno")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            consultar_aluno(alunos)
        elif opcao == "4":
            excluir_aluno(alunos)
        elif opcao == "0":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
