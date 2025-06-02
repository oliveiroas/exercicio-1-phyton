import json
import os

db_clientes = "db_clientes.json"

def carregar_dados():
    if os.path.exists(db_clientes):
        with open(db_clientes, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []

def adicionar_cadastro(nome, cpf, rg, data_nascimento, endereco, cidade, estado, telefone, celular, email): 
    cadastro = {
        "nome": nome,
        "cpf": cpf,
        "rg": rg,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "cidade": cidade,
        "estado": estado,
        "telefone": telefone,
        "celular": celular,
        "email": email
    }
    return cadastro

def obter_dados_cadastro():
    nome_ = input("INFORME O NOME COMPLETO PARA O CADASTRO: ")
    cpf = input("INFORME O CPF PARA O CADASTRO: ")
    rg = input("INFORME O RG PARA O CADASTRO: ")
    data_nascimento = input("INFORME A DATA DE NASCIMENTO PARA O CADASTRO (DD/MM/AAAA): ")
    endereco = input("INFORME O ENDEREÇO PARA O CADASTRO: ")
    cidade = input("INFORME A CIDADE PARA O CADASTRO: ")
    estado = input("INFORME O ESTADO PARA O CADASTRO: ")
    telefone = input("INFORME O TELEFONE PARA O CADASTRO: ")
    celular = input("INFORME O CELULAR PARA O CADASTRO: ")
    email_cadastro = input("INFORME O EMAIL PARA O CADASTRO: ")

    return adicionar_cadastro(nome_, cpf, rg, data_nascimento, endereco, cidade, estado, telefone, celular, email_cadastro)

def salvar_dados(cadastros):
    with open(db_clientes, "w", encoding="utf-8") as arq_json:
        json.dump(cadastros, arq_json, indent=4, ensure_ascii=False)

def mostrar_dados_cadastros(dados_cadastros):
    if not dados_cadastros:
        print("Nenhum cadastro encontrado.")
    else:
        for cadastro in dados_cadastros:
            print(f"Nome: {cadastro['nome']} | CPF: {cadastro['cpf']} | RG: {cadastro['rg']} | Data de Nascimento: {cadastro['data_nascimento']} | Endereço: {cadastro['endereco']} | Cidade: {cadastro['cidade']} | Estado: {cadastro['estado']} | Telefone: {cadastro['telefone']} | Celular: {cadastro['celular']} | Email: {cadastro['email']}")

def iniciar_sistema():
    cadastros = carregar_dados()
    while True:
        print("=" * 80)
        print("Opção 1 => Mostrar Lista de Cadastros.")
        print("Opção 2 => Cadastrar novo cadastro.")
        print("Opção 3 => Sair do Sistema.")
        print("=" * 80)
        
        opcao = input("ESCOLHA UMA DAS OPÇÕES ACIMA: ")

        if opcao == "1":
            mostrar_dados_cadastros(cadastros)
        elif opcao == "2":
            novo_cadastro = obter_dados_cadastro()
            cadastros.append(novo_cadastro)
            salvar_dados(cadastros)
        elif opcao == "3":
            print("Sistema finalizado.")
            break
        else:
            print("Opção inválida, escolha uma das opções no menu.")
if __name__ == "__main__":
    iniciar_sistema()
