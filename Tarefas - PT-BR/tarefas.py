import json
import os

ARQUIVO = "dados_tarefas.json"


def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r") as f:
                return json.load(f)
        except:
            return []
    return []


def salvar_tarefas():
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)


tarefas = carregar_tarefas()


def mostrar_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\nLista de tarefas:")
    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["concluida"] else "✘"
        print(f"{i} - {tarefa['nome']} [{status}]")


def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    tarefas.append({"nome": nome, "concluida": False})
    salvar_tarefas()  # ← AGORA SALVA
    print("Tarefa adicionada!")


def concluir_tarefa():
    mostrar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para concluir: "))
        tarefas[indice]["concluida"] = True
        salvar_tarefas()  # ← SALVA
        print("Tarefa concluída!")
    except:
        print("Índice inválido.")


def remover_tarefa():
    mostrar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para remover: "))
        tarefas.pop(indice)
        salvar_tarefas()  # ← SALVA
        print("Tarefa removida!")
    except:
        print("Índice inválido.")


while True:
    print("\n--- MENU ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        mostrar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
