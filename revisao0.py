import json
import os

db_roupas_path = 'cadastro_roupas.json'

def carregar_dados():
    if os.path.exists(db_roupas_path):
        with open(db_roupas_path, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

def obter_dados():
    db_roupas = carregar_dados()

    while True:
        nome_roupa = input("Informe o nome da roupa: ")
        descricao_roupa = input("Informe a descrição da roupa: ")
        tamanho = input("Informe o tamanho da roupa (P/M/G/EG): ")
        cor = input("Informe a cor da roupa: ")

        try:
            valor = float(input("Informe o valor da roupa: "))
            quantidade = int(input("Informe a quantidade da roupa: "))
        except ValueError:
            print("Por favor, digite valores numéricos válidos para valor e quantidade.")
            continue

        if not nome_roupa or not descricao_roupa or not tamanho or not cor:
            print("\nTodos os campos precisam ser preenchidos.\n")
        else:
            data_roupa = {
                "id_roupa": len(db_roupas) + 1,
                "nome_roupa": nome_roupa,
                "descricao_roupa": descricao_roupa,
                "tamanho": tamanho,
                "cor": cor,
                "valor": valor,
                "quantidade": quantidade
            }
            return data_roupa

def cadastrar_roupa(receber_roupa):
    if not isinstance(receber_roupa, dict):
        print("\nNão foi possível cadastrar a roupa. Os dados fornecidos são inválidos.")
        return

    db_roupas = carregar_dados()

    db_roupas.append(receber_roupa)

    with open(db_roupas_path, "w", encoding="utf-8") as arq_json:
        json.dump(db_roupas, arq_json, indent=4, ensure_ascii=False)

    print("Cadastro realizado com sucesso.")

def mostrar_roupas(db_roupas):
    if db_roupas:
        for roupa in db_roupas:
            print(f"""
                ID da Roupa: {roupa["id_roupa"]}
                Nome da Roupa: {roupa["nome_roupa"]}
                Descrição da Roupa: {roupa["descricao_roupa"]}
                Tamanho: {roupa["tamanho"]}
                Cor: {roupa["cor"]}
                Valor: {roupa["valor"]}
                Quantidade: {roupa["quantidade"]}
            """)
    else:
        print("Não existe nenhuma roupa cadastrada.")

def iniciar_sistema():
    db_roupas = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("Opção 1 - Mostrar Lista de Roupas")
        print("Opção 2 - Cadastrar Roupa")
        print("Opção 3 - Sair do Sistema.")
        print("="*80)

        opcao = input("Escolha uma das opções no menu: ")

        if opcao == "1":
            mostrar_roupas(db_roupas)
        elif opcao == "2":
            cadastrar_roupa(obter_dados())
        elif opcao == "3":
            print("Sistema finalizado!!!")
            break
        else:
            print("Opção inválida, escolha uma das opções no menu.")

iniciar_sistema()
