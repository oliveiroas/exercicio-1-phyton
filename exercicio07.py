from exercicio04 import calcular_media

cadastros = []

def obter_dados_cadastro():
    nome_ = input("INFORME O NOME COMPLETO PARA O CADASTRO: ")
    cpf = int(input("INFORME O CPF PARA O CADASTRO: "))
    rg = int(input("INFORME O RG PARA O CADASTRO: "))
    data_nascimento = input("INFORME A DATA DE NASCIMENTO PARA O CADASTRO (DD/MM/AAAA): ")
    endereco = input("INFORME O ENDEREÇO PARA O CADASTRO: ")
    cidade = input("INFORME A CIDADE PARA O CADASTRO: ")
    estado = input("INFORME O ESTADO PARA O CADASTRO: ")
    telefone = input("INFORME O TELEFONE PARA O CADASTRO: ")
    celular = input("INFORME O CELULAR PARA O CADASTRO: ")
    email_cadastro = input("INFORME O EMAIL PARA O CADASTRO: ")

    return adicionar_cadastro(nome_, cpf, rg, data_nascimento, endereco, cidade, estado, telefone, celular, email_cadastro)

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
    cadastros.append(cadastro)

    return cadastros

def mostrar_dados_cadastros(dados_cadastros):
    for cadastro in dados_cadastros:
        print(f"Nome: {cadastro['nome']} | CPF: {cadastro['cpf']} | RG: {cadastro['rg']} | Data de Nascimento: {cadastro['data_nascimento']} | Endereço: {cadastro['endereco']} | Cidade: {cadastro['cidade']} | Estado: {cadastro['estado']} | Telefone: {cadastro['telefone']} | Celular: {cadastro['celular']} | Email: {cadastro['email']}")
    return 

def iniciar_sistema():
    while True:
        print("="*80)
        print("Opção 1 => Mostrar Lista Para cadastros cadastrados.")
        print("Opção 2 => Cadastrar novo cadastro.")
        print("Opção 3 => Sair Para o Sistema.")
        print("="*80)
        
        opcao = input("ESCOLHA UMA DAS OPÇÕES ACIMA: ")

        if opcao == "1":
            mostrar_dados_cadastros(cadastros)
        elif opcao == "2":
            obter_dados_cadastro()
        else:
            print("Sistema finalizado")
            break
        

iniciar_sistema()
