 
import json
import os

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    """Carrega as tarefas salvas no arquivo JSON."""

    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)

        except (json.JSONDecodeError, OSError):
            print("Não foi possível carregar as tarefas.")

    return [
        {"nome": "Estudar Python", "concluida": False},
        {"nome": "Fazer exercícios", "concluida": False}
    ]


def salvar_tarefas():
    """Salva as tarefas no arquivo JSON."""

    try:
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

    except OSError:
        print("Erro ao salvar as tarefas.")


def adicionar_tarefa():
    """Adiciona uma nova tarefa."""

    nova_tarefa = input("Digite uma nova tarefa: ").strip()

    if nova_tarefa == "":
        print("Você precisa digitar o nome da tarefa!")
        return

    tarefas.append({
        "nome": nova_tarefa,
        "concluida": False
    })

    salvar_tarefas()
    print("Sua tarefa foi adicionada!")


def listar_tarefas():
    """Exibe todas as tarefas."""

    print("\n=== STATUS DAS TAREFAS ===")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):

        if tarefa["concluida"]:
            status = "Concluída"
        else:
            status = "Pendente"

        print(f"{numero} - {tarefa['nome']} - {status}")


def concluir_tarefa():
    """Marca uma tarefa como concluída."""

    if not tarefas:
        print("Não existem tarefas para concluir.")
        return

    listar_tarefas()

    numero = input("\nQual tarefa deseja concluir? ").strip()

    if not numero.isdigit():
        print("Digite apenas números!")
        return

    numero = int(numero)

    if numero < 1 or numero > len(tarefas):
        print("Número de tarefa inválido!")
        return

    tarefa = tarefas[numero - 1]

    if tarefa["concluida"]:
        print("Essa tarefa já está concluída!")
        return

    tarefa["concluida"] = True

    salvar_tarefas()

    print("Tarefa marcada como concluída!")


def exibir_menu():
    """Exibe as opções do programa."""

    print("\n=== ORGANIZADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Sair")


tarefas = carregar_tarefas()

opcao = ""

while opcao != "4":

    exibir_menu()

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar_tarefa()

    elif opcao == "2":
        listar_tarefas()

    elif opcao == "3":
        concluir_tarefa()

    elif opcao == "4":
        print("Programa encerrado!")

    else:
        print("Opção inválida!")
