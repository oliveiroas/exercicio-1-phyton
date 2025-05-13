from exercicio04 import calcular_media

alunos = []

def obter_dados_alunos():
    nome_aluno = input("INFORME O NOME COMPLETO DO ALUNO:")
    email_aluno = input("INFORME O EMAIL DO ALUNO:")
    serie_aluno = input("INFORME A SERIE DO ALUNO:")
    nota01_aluno = input("INFORME A PRIMEIRA NOTA DO ALUNO:")
    nota02_aluno = input("INFORME A SEGUNDA NOTA DO ALUNO:")
    nota03_aluno = input("INFORME A TERCEIRA NOTA DO ALUNO:")

    return adicionar_aluno(nome_aluno, email_aluno, serie_aluno, nota01_aluno, nota02_aluno, nota03_aluno)


def adicionar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0): 

    notas = [nota01, nota02, nota03]    

    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "nota": notas,
        "media": calcular_media
    }
    alunos.append(aluno)

    return alunos

def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
        print(f"Nome Do Aluno: {aluno["nome"]} ) | Email do aluno: {aluno["email"]} | Série do aluno {aluno["serie"]} | Notas do aluno{aluno["notas"]} Média do aluno {aluno["media"]}")
    return 


def iniciar_sistema():
    while True:
        print("="*80)
        print("Opcao 1 => Mostrar Lista De alunos cadastrados.")
        print("Opcao 2 => Cadastrar Alunos.")
        print("Opcao 3 => Sair Do Sistema.")
        print("="*80)
        
        opcao = input("ESCOLHA UMAS DAS OPCOES ACIMA: ")

        if opcao == "1":
            mostrar_dados_alunos(alunos)
        elif opcao == "2":
            obter_dados_alunos()
        else:
            print("Sistema fizalizado")
            break
        

iniciar_sistema()

