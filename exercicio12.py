import json
import os

db_agendamentos = "db_agendamentos.json"

def carregar_dados():
    if os.path.exists(db_agendamentos):
        with open(db_agendamentos, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

def obter_dados_agendamento():
    nome_cliente = input("Informe o Nome do Cliente: ")
    servico_desejado = input("Informe o Serviço Desejado: ")
    data_agendamento = input("Informe a Data do Agendamento (DD/MM/AAAA): ")
    horario_agendamento = input("Informe o Horário do Agendamento (HH:MM): ")

    agendamento = {
        "nome": nome_cliente,
        "servico": servico_desejado,
        "data": data_agendamento,
        "horario": horario_agendamento
    }

    return agendamento

def cadastrar_agendamento(dados_agendamento):
    agendamentos = carregar_dados()
    agendamentos.append(dados_agendamento)

    with open(db_agendamentos, "w", encoding="utf-8") as arq_json:
        json.dump(agendamentos, arq_json, indent=4, ensure_ascii=False)

def mostrar_dados_agendamentos(agendamentos):
    if not agendamentos:
        print("Nenhum agendamento cadastrado no momento.")
    else:
        for agendamento in agendamentos:
            print(f"""
            Nome do Cliente: {agendamento["nome"]}
            Serviço Desejado: {agendamento["servico"]}
            Data do Agendamento: {agendamento["data"]}
            Horário do Agendamento: {agendamento["horario"]}
            """)

def iniciar_sistema():
    agendamentos = carregar_dados()
    while True:
        print("")
        print("=" * 80)
        print("Opção 1 - Mostrar Lista de Agendamentos")
        print("Opção 2 - Cadastrar Agendamento")
        print("Opção 3 - Sair do Sistema")
        print("=" * 80)

        opcao = input("Escolha uma das opções do Menu: ")

        if opcao == "1":
            mostrar_dados_agendamentos(agendamentos)
        elif opcao == "2":
            cadastrar_agendamento(obter_dados_agendamento())
            agendamentos = carregar_dados()
        elif opcao == "3":
            print("Sistema Finalizado")
            break
        else:
            print("Opção inválida, escolha uma das opções no menu.")

if __name__ == "__main__":
    iniciar_sistema()
