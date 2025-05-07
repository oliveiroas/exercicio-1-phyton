

def adicionar_aluno(nome, email, serie, nota01, nota02, nota03,):
    dados_alunos = []  
    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "nota": [nota01, nota02, nota03]
    }
    dados_alunos.append(aluno)
    return dados_alunos

print(adicionar_aluno("Vinicius", "viniciuscabulosao@gmail.com", "2b série", 10, 10, 10))




