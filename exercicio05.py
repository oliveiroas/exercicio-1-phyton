from exercicio04 import calcular_media

def adicionar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0): 
    alunos = []

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

print(adicionar_aluno("Vinicius", "viniciuscabulosao@gmail.com", "2b série"))

